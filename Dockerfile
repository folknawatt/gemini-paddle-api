# 1. Base Image
FROM python:3.13

# 2. Working Directory
WORKDIR /wrk/app

RUN apt-get update && apt-get install -y \
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
    lzma \ 
    wget \
    libgl1 \
    # python3-opencv \
    && apt-get clean

# 3. คัดลอกไฟล์ Dependencies
COPY pyproject.toml .
RUN pip install --no-cache-dir .
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# 4. คัดลอกโค้ดโปรเจกต์
# คัดลอกไฟล์ที่เหลือทั้งหมด (. ในที่นี้หมายถึง FOLDER ปัจจุบัน) เข้าไปใน /wrk/app
COPY . /wrk/app


#---------------------------------------------------------------------------------------------
WORKDIR /wrk/app/src

# # 5. บอก Docker ว่าแอปฯ ของเราจะรันที่ Port ไหน

# # 6. คำสั่งที่ใช้รันแอปฯ
# # นี่คือคำสั่งเดียวกับที่คุณรัน uvicorn ปกติ
# # "main:app" คือ: ให้รันตัวแปร "app" ที่อยู่ในไฟล์ "main.py"
# # "--host 0.0.0.0" คือ: อนุญาตให้ traffic จากภายนอก container เข้ามาได้ (สำคัญมาก!)
# # "--port 8000" คือ: รันที่ port 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

