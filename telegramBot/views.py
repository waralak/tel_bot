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

    if request.method == "POST":
        return HttpResponse("POSted")
    
    try:
        update = telegram.Update.de_json(request.POST, bot)
    except:
        return HttpResponse("1111\n")

    try:
        chat_id = update.message.chat.id
    except:
        return HttpResponse("2222\n")

    try:
        msg_id = update.message.message_id
    except:
        return HttpResponse("3333\n")

    print("Message Successfully Received from {}.{}".format(chat_id, msg_id))
    bot_welcome = "HIIIIII"
    bot.sendMessage(chat_id=chat_id, text=bot_welcome, reply_to_message_id=msg_id)
    return HttpResponse("")
