import os
import requests
import schedule
import time
import asyncio
from telegram import Bot
import openai
from dotenv import load_dotenv

# ========== LOAD ENVIRONMENT VARIABLES ==========
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Quick check
if not TELEGRAM_TOKEN or not CHAT_ID or not NEWS_API_KEY or not OPENAI_API_KEY:
    raise Exception("One or more environment variables are missing in .env!")

bot = Bot(token=TELEGRAM_TOKEN)
openai.api_key = OPENAI_API_KEY

# ========== FETCH NEWS ==========
def get_news():
    url = f"https://newsapi.org/v2/top-headlines?country=us&pageSize=4&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    print("NewsAPI status code:", response.status_code)
    print("NewsAPI response:", response.text[:500])  # print first 500 chars only

    try:
        data = response.json()
        articles = data.get("articles", [])
        print("Number of articles fetched:", len(articles))
        return [{"title": a["title"], "url": a["url"], "description": a["description"] or ""} for a in articles]
    except Exception as e:
        print("Error parsing JSON:", e)
        return []
# ========== SUMMARIZE NEWS ==========
def summarize_article(article):
    """Summarize the article using OpenAI GPT"""
    try:
        prompt = f"Summarize the following news in 5-10 lines:\nTitle: {article['title']}\nDescription: {article['description']}\nURL: {article['url']}"

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes news."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=250,
            temperature=0.5
        )

        summary = response.choices[0].message.content.strip()
        return summary
    except Exception as e:
        print("Error summarizing article:", e)
        return article["title"] + " (Summary not available)"


# ========== SEND TO TELEGRAM ==========
async def send_news():
    articles = get_news()
    if not articles:
        await bot.send_message(chat_id=CHAT_ID, text="⚠️ Couldn't fetch news today.")
        print("❌ Failed to fetch news.")
        return

    messages = []
    for i, article in enumerate(articles, 1):
        summary = summarize_article(article)
        messages.append(f"{i}. {summary}\nRead more: {article['url']}\n")

    full_message = "📰 Today's Top News Summaries:\n\n" + "\n".join(messages)
    await bot.send_message(chat_id=CHAT_ID, text=full_message)
    print("✅ News sent successfully!")

# ========== SCHEDULE DAILY ==========
def job():
    asyncio.run(send_news())

schedule.every().day.at("08:00").do(job)

print("🤖 Telegram News Bot is running... (Press CTRL+C to stop)")

# Run once immediately
job()

while True:
    schedule.run_pending()
    time.sleep(60)
