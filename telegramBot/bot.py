from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ApplicationBuilder

import os

async def start(update: Update, context: CallbackContext):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="I am a bot! Hi!"
    )

application = ApplicationBuilder().token(os.getenv("TOKEN")).build()
start_handler = CommandHandler('start', start)

application.add_handler(start_handler)
application.run_polling()


