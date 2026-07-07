import os
from dotenv import load_dotenv
load_dotenv()
TELEGRAM_BOT_TOKEN=os.getenv("TELEGRAM_BOT_TOKEN")
GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
MODEL_NAME="gemini-2.5-flash"
