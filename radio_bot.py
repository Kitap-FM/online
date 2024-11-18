import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

radio_streaming = False
radio_url = "http://radio.tatmedia.com:8800/kitapfm"

async def start_radio(update: Update, context: CallbackContext) -> None:
    global radio_streaming
    if radio_streaming:
        await update.message.reply_text("Радио кушылган!")
        return
    radio_streaming = True
    await update.message.reply_text(f"Радионы кушам! \nМонда: {radio_url}")

async def stop_radio(update: Update, context: CallbackContext) -> None:
    global radio_streaming
    if not radio_streaming:
        await update.message.reply_text("Радио кушылмаган.")
        return
    radio_streaming = False
    await update.message.reply_text("Радионы туктатам")

async def main() -> None:

    telegram_token = os.getenv("TELEGRAM_API_TOKEN")
