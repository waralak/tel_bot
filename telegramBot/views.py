from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt

import telegram
import os
import logging
import json

TOKEN = os.environ.get("TOKEN", "")
bot = telegram.Bot(token=TOKEN)
PHOTO = "https://c.tenor.com/yheo1GGu3FwAAAAd/rick-roll-rick-ashley.gif"

# For debugging 
logger = logging.getLogger('testlogger')

@csrf_exempt
def index(request):
    try:
        js = request.read().decode()
        logger.info('\n{}\n'.format(js))
        js = json.loads(js)

        update = telegram.Update.de_json(js, bot)
        #chat_id = update.message.chat.id
        #msg_id = update.message.message_id

        logger.info("Successfully turned into telegram object")

        bot_welcome = "Accepted"
        update.message.reply_text(bot_welcome)
        #bot.sendMessage(chat_id=chat_id, text=bot_welcome, reply_to_message_id=msg_id)
        #bot.send_animation(chat_id, PHOTO, caption='LMAOOOO')

        logger.info("Successfully turned into sent object")
    except Exception as e:
        logger.info("\n{}\n".format(e))

    return HttpResponse("")


@csrf_exempt
def set_webhook(request):
    if not request.method == "POST":
        raise Http404("")

    try:
        password = request.POST.get("password", "")

        if not password:
            raise Http404("")

        if password != os.environ.get("SECRET_PASSWORD", "default"):
            raise Http404("")

        bot.delete_webhook()
        bot.set_webhook(
            url="https://telbotingg.herokuapp.com/{}/".format(TOKEN)
        )

    except Exception as e:
        logger.info("\n{}\n".format(e))

    return HttpResponse("\nWebhook Setup OK\n")
