from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import telegram
import os
import sys

bot = telegram.Bot(token=os.environ.get("TOKEN", ""))

def index(request):
    if request.method == "GET":
        return HttpResponse("")
    
    update = telegram.Update.de_json(request.POST, bot)
    
    chat_id = update.message.chat.id
    msg_id = update.message.message_id

    print("Message Successfully Received from {}.{}".format(chat_id, msg_id))


    return HttpResponse("")
