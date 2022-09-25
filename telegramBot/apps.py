from django.apps import AppConfig
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

class TelegrambotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'telegramBot'

    def ready(self):
        from . import bot

        
