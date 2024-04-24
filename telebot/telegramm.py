import logging
import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from django.core.management import execute_from_command_line
from movie.models import Film
from cinema.models import Seans
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

TOKEN = '6855554419:AAGOFwK1AwjJxaKuiCqTM0PNUQTCuq2LgYA'

bot = telegram.Bot(token=TOKEN)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def films(update, context):
    films = Film.objects.all()
    if films:
        message = 'Список доступных фильмов:\n'
    else:
        message = 'На данный момент фильмы отсутствуют в базе данных.'

        update.message.reply_text(message)

def seances(update, context):
    seances = Seans.objects.all()
    if seances:
        message = "Список доступных сеансов:\n"
        for seans in seances:
            message += f"- {seans.film.title} в {seans.hall.name} ({seans.start_time})\n"
    else:
        message = "На данный момент сеансы отсутствуют в базе данных."
    
    update.message.reply_text(message)


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher   

    dp.add_handler(CommandHandler("films", films))
    dp.add_handler(CommandHandler("seances", seances))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()