from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import telegram
import os

bot = telegram.Bot(token=os.environ.get("TOKEN", "")

def index(request):
    update = telegram.Update.de_json(request.POST, bot)
    
    chat_id = update.message.chat.id
    msg_id = update.message.message_id

    print("Message Successfully Received from {}.{}".format(chat_id, msg_id))

    return HttpResponse("")
