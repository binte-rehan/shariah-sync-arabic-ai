from telegram import Update
from telegram.ext import ContextTypes
from ai.gemini import ask_ai
async def handle_message(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(ask_ai(update.message.text))
