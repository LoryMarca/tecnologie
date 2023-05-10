TOKEN="6131316606:AAEPAdSdE3cd0rTciMEDKSa5zUxQvlLlHks"

import requests
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, filters
import myTelegram
import time

t = myTelegram.myTelegram(TOKEN)

while True:
    messages = t.getUpdates()
    if len(messages) > 0:
        for messaggio in messages:
            if str(messaggio["message"]["text"]).lower().find("ciao")!=-1:
                t.sendMessage(messaggio["message"]["chat"]["id"], "ciao anche a te")
    time.sleep(1)

exit()
# Inizializzazione del bot Telegram
bot = telegram.Bot(TOKEN)

# Definizione della funzione per gestire il comando "/start"
def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Ciao! Benvenuto in lilmarcat bot.")

# Definizione della funzione per gestire i messaggi di testo
def echo(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

# Definizione della funzione per gestire i messaggi di immagini
def image(update, context):
    photo_file = context.bot.get_file(update.message.photo[-1].file_id)
    photo_file.download('photo.jpg')
    context.bot.send_message(chat_id=update.message.chat_id, text="Ho ricevuto la tua foto!")



# Inizializzazione del gestore degli aggiornamenti del bot
update = bot.getUpdates()
print(update)
exit()

# Definizione dei gestori per i comandi e i messaggi
start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(filters.text & (~filters.command), echo)
image_handler = MessageHandler(filters.photo, image)

# Aggiunta dei gestori all'updater
updater.dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(echo_handler)
updater.dispatcher.add_handler(image_handler)

# Avvio del bot
updater.start_polling()
updater.idle

