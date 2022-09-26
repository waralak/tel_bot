from django.apps import AppConfig

class TelegrambotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'telegramBot'

    def ready(self):
        from . import bot

        
