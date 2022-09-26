import telegram
import os

TOKEN = os.environ.get("TOKEN", "")
bot = telegram.Bot(token=TOKEN)

bot.set_webhook(url="https://telboting.herokuapp.com/{}".format(TOKEN))

