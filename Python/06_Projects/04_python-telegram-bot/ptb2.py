from telegram.ext import CommandHandler
from telegram.ext import CallbackContext
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
from telegram import Update
import logging


TOKEN = '5017969562:AAGZtaIlwmzCzaO4bpEUvCl5PL6dpJ6ZsfE'
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def start(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


def echo(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


def caps(update: Update, context: CallbackContext):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


def unknown(update: Update, context: CallbackContext):
    msg = "Sorry, I didn't understand that command."
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg)


start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
caps_handler = CommandHandler('caps', caps)
unknown_handler = MessageHandler(Filters.command, unknown)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(caps_handler)
dispatcher.add_handler(unknown_handler)

updater.start_polling()



