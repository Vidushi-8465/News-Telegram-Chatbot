import os
from dotenv import load_dotenv

load_dotenv()  # loads .env from current folder

print("TELEGRAM_TOKEN =", os.getenv("TELEGRAM_TOKEN"))
print("CHAT_ID =", os.getenv("CHAT_ID"))
print("NEWS_API_KEY =", os.getenv("NEWS_API_KEY"))
print("OPENAI_API_KEY =", os.getenv("OPENAI_API_KEY"))
