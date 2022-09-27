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
    
    logger.info('\n{}\n'.format(request.read()))
    try:
        js = json.loads(request.read().decode())

        logger.info("Successfully turned into json object")
        
        update = telegram.Update.de_json(js, bot)
        chat_id = update.message.chat.id
        msg_id = update.message.message_id

        logger.info("Successfully turned into telegram object")

        logger.info("Message Successfully Received from {}.{}".format(chat_id, msg_id))
        bot_welcome = "HIIIIII"
        bot.sendMessage(chat_id=chat_id, text=bot_welcome, reply_to_message_id=msg_id)

        logger.info("Successfully turned into sent object")
    except Exception as e:
        logger.info("\n{}\n".format(e))
    return HttpResponse("")
