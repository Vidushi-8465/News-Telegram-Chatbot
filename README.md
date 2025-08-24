# Telegram News Bot

A simple **Telegram chatbot** that fetches the latest news using [NewsAPI](https://newsapi.org/) and summarizes articles using [OpenAI GPT models](https://platform.openai.com/).  
It delivers short, easy-to-read summaries directly in your Telegram chat. 

---

##  Features

-  Fetches **top headlines** from NewsAPI.  
-  **Summarizes articles** into short, crisp points using OpenAI.  
-  Runs on **Telegram** – easy to chat with the bot.  
-  Secure API key handling with `.env` file.  
-  Works on any laptop (Windows/Mac/Linux) with Python.  

---

## Installation & Setup

1. Clone the Repository
```bash
git clone https://github.com/<your-username>/telegram-news-bot.git
cd telegram-news-bot
```

Step 2: Create & Activate Virtual Environment (optional but recommended)
```
# Create Virtual Environment
python -m venv venv
 On Windows:
venv\Scripts\activate
 On Mac/Linux:
source venv/bin/activate
```

Step 3: Install Requirements
```
pip install -r requirements.txt
 Setup API Keys
```
Step 4: Configure Environment Variables
```
Copy .env.example and rename it to .env.
Add your keys inside:
TELEGRAM_BOT_TOKEN=your-telegram-bot-token
NEWS_API_KEY=your-newsapi-key
Run the Bot
```

Step 5: Start the Bot
```
python src/main.py
```

🛠️ Project Structure
``` 
telegram-news-bot/<br>
│── .env.example        # Example environment variables<br>
│── requirements.txt    # Dependencies<br>
│── README.md           # Documentation<br>
│── src/<br>
    ├── main.py         # Main bot logic<br>
    ├── test_env.py     # Test environment setup<br>
    ├── test_news.py    # Test News API fetching<br>
```

Notes

Make sure you have Python 3.8+ installed.<br>
Keep your .env file private (don’t push it to GitHub).<br>
You can extend the bot by adding more categories or filters.<br>

 Contributing
 
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.
