from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import telegram
import os
import logging
import json
from django.views.decorators.csrf import csrf_exempt

bot = telegram.Bot(token=os.environ.get("TOKEN", ""))
logger = logging.getLogger('testlogger')

@csrf_exempt
def index(request):
    if request.method == "GET":
        return HttpResponse("")
    
    logger.info('\nLength of the POST request: {}\n'.format(request.read()))

    js = json.loads(request.read())
    
    try:
        update = telegram.Update.de_json(js, bot)
    except Exception as e:
        logger.info('\n{}\n'.format(e))
        return HttpResponse("1111 {}\n".format(e))

    try:
        chat_id = update.message.chat.id
    except Exception as e:
        logger.info('\n{}\n'.format(e))
        return HttpResponse("2222 {}\n".format(e))

    try:
        msg_id = update.message.message_id
    except Exception as e:
        logger.info('\n{}\n'.format(e))
        return HttpResponse("{}\n".format(e))

    print("Message Successfully Received from {}.{}".format(chat_id, msg_id))
    bot_welcome = "HIIIIII"
    bot.sendMessage(chat_id=chat_id, text=bot_welcome, reply_to_message_id=msg_id)
    return HttpResponse("")
