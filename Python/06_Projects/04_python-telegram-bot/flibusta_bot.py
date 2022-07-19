#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

"""
Basic example for a bot that uses inline keyboards. For an in-depth explanation, check out
 https://github.com/python-telegram-bot/python-telegram-bot/wiki/InlineKeyboard-Example.
"""
import logging
import flib
import json

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
from telegram.ext import MessageHandler, Filters


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)



def start_callback(update: Update, context: CallbackContext):
    update.message.reply_text("Введите название книги (без автора): ")


def find_the_book(update: Update, context: CallbackContext) -> None:
    search_string = update.message.text
    update.message.reply_text("Вы ищите " + search_string)
    
    books_j = flib.scrape_books(search_string)
    books = json.loads(books_j)

    kb = []
    for i in range(len(books)):
        text = books[str(i)]['content']['title']
        callback_data = 'find_book_by_id ' + books[str(i)]['id']
        kb.append([InlineKeyboardButton(text, callback_data=callback_data)])

    reply_markup = InlineKeyboardMarkup(kb)

    update.message.reply_text('Please choose:', reply_markup=reply_markup) # DONE:



def button(update: Update, context: CallbackContext) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()

    query.edit_message_text(text=f"Вы выбрали опцию: {query.data}")
    command, id = query.data.split(' ', maxsplit=2)
    command(id)

def help_command(update: Update, context: CallbackContext) -> None:
    """Displays info on how to use the bot."""
    update.message.reply_text("Нажмие /start чтобы начать")


def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    TOKEN = '5017969562:AAGZtaIlwmzCzaO4bpEUvCl5PL6dpJ6ZsfE'
    updater = Updater(TOKEN)

    updater.dispatcher.add_handler(CommandHandler('start', start_callback))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help_command))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, find_the_book))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()
