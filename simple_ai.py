import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY1")

model = init_chat_model(
    model="gemini-3-flash",
    model_provider="google-genai",
    api_key=GOOGLE_API_KEY
)