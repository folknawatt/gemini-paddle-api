# Stage 1: Build Stage
ARG PYTHON_BASE=3.13-slim
FROM python:${PYTHON_BASE} AS builder

# ป้องกันการสร้าง .pyc files และบังคับให้ output ไม่ถูก buffer
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /build

# ติดตั้ง uv ด้วย pip แบบไม่เก็บ cache
RUN pip install --no-cache-dir uv

# ติดตั้ง build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    zlib1g-dev \
    libncurses5-dev \
    libgdbm-dev \
    libnss3-dev \
    libssl-dev \
    libsqlite3-dev \
    libreadline-dev \
    libffi-dev \
    libbz2-dev \
    liblzma-dev \
    wget \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*


# Copy เฉพาะไฟล์ dependencies ก่อน
COPY pyproject.toml uv.lock ./

# ติดตั้ง dependencies ไปที่ virtual environment เพื่อแยกจาก system packages
RUN uv venv /opt/venv && \
    . /opt/venv/bin/activate && \
    uv pip install --no-cache .

#---------------------------------------------------------------------------------------------
# Stage 2: Runtime Stage
FROM python:${PYTHON_BASE}

# ติดตั้ง runtime dependencies เท่านั้น (ไม่ใช่ build tools)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app

# Copy virtual environment จาก builder stage
COPY --from=builder /opt/venv /opt/venv

# Copy src (Source Code folder)
COPY . .

# ตั้งค่า PATH ให้ใช้ virtual environment
ENV PATH="/opt/venv/bin:$PATH" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1


WORKDIR /app/src

# Expose port (เป็น metadata สำหรับ documentation)
EXPOSE 8000

# ใช้ uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
