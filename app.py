import logging
from telegram.ext import Application,CommandHandler,MessageHandler,filters
from config import TELEGRAM_BOT_TOKEN
from bot.commands import start
from bot.handlers import handle_message
logging.basicConfig(level=logging.INFO)
app=Application.builder().token(TELEGRAM_BOT_TOKEN).build()
app.add_handler(CommandHandler("start",start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,handle_message))
app.run_polling()
