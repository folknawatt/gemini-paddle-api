from google import genai
from dotenv import load_dotenv
import os

load_dotenv()


prompt = "Explain how AI works in a few words"


def gen_content(prompt=None):

    client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text


if __name__ == "__main__":
    print(gen_content(prompt))
