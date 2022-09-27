from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import telegram
import os
import sys
from django.views.decorators.csrf import csrf_exempt

bot = telegram.Bot(token=os.environ.get("TOKEN", ""))


@csrf_exempt
def index(request):
    if request.method == "GET":
        return HttpResponse("")
    
    update = telegram.Update.de_json(request.POST, bot)
    
    chat_id = update.message.chat.id
    msg_id = update.message.message_id

    print("Message Successfully Received from {}.{}".format(chat_id, msg_id))
    bot_welcome = "HIIIIII"
    bot.sendMessage(chat_id=chat_id, text=bot_welcome, reply_to_message_id=msg_id)
    return HttpResponse("")
