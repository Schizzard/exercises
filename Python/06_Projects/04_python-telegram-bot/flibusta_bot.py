#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

"""
Basic example for a bot that uses inline keyboards. For an in-depth explanation, check out
 https://github.com/python-telegram-bot/python-telegram-bot/wiki/InlineKeyboard-Example.
"""
import logging
import flib
import os

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
from telegram.ext import MessageHandler, Filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

lib = []


def start_callback(update: Update, context: CallbackContext):
    update.message.reply_text("Введите название книги (без автора) ИЛИ добавьте фамилию автора на новой строке. \n\nПример:\n\n1984\nОруэлл")


def find_the_book(update: Update, context: CallbackContext) -> None:
    search_string = update.message.text

    if '\n' in search_string:
        title, author = search_string.split('\n', maxsplit=1)
        libr = flib.scrape_books_mbl(title, author)
    else:
        libr = flib.scrape_books(search_string)

    if libr is None:
        update.message.reply_text('К сожалению, ничего не найдено =(')
    else:
        kb = []
        for i in range(len(libr)):
            book = libr[i]
            text = f'{book.title} - {book.author}'
            callback_data = 'find_book_by_id ' + book.id
            kb.append([InlineKeyboardButton(text, callback_data=callback_data)])

        reply_markup = InlineKeyboardMarkup(kb)

        update.message.reply_text('Выберите книгу:', reply_markup=reply_markup)  # DONE:


def button(update: Update, context: CallbackContext) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()

    command, arg = query.data.split(' ', maxsplit=1)
    if command == 'find_book_by_id':
        find_book_by_id(book_id=arg, update=update, context=context)
    if command == 'get_book_by_format':
        get_book_by_format(data=arg, update=update, context=context)


def find_book_by_id(book_id, update: Update, context: CallbackContext):
    book = flib.get_book_by_id(book_id)
    capt = u'\U0001F4D6 {title}\n\U0001F5E3 {author}'.format(author=book.author, title=book.title)

    kb = []
    for b_format in book.formats:
        text = b_format
        callback_data = f'get_book_by_format {book.id}+{b_format}'
        kb.append([InlineKeyboardButton(text, callback_data=callback_data)])
    reply_markup = InlineKeyboardMarkup(kb)

    if book.cover:
        flib.download_book_cover(book)
        c_full_path = os.path.join(os.getcwd(), "books", book_id, 'cover.jpg')
        cover = open(os.path.join(c_full_path), "rb")
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=cover, caption=capt,
                               reply_markup=reply_markup)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text='[обложки нет]\n\n' + capt,
                                 reply_markup=reply_markup)


def get_book_by_format(data: str, update: Update, context: CallbackContext):
    mes = context.bot.send_message(chat_id=update.effective_chat.id, text=f"Подождите, идёт скачивание...")

    book_id, book_format = data.split('+')
    book = flib.get_book_by_id(book_id)

    b_full_path = flib.download_book(book, book_format)
    file = open(os.path.join(b_full_path), "rb")
    context.bot.send_document(chat_id=update.effective_chat.id, document=file)
    context.bot.deleteMessage(chat_id=mes.chat_id, message_id=mes.message_id)


def help_command(update: Update, context: CallbackContext) -> None:
    """Displays info on how to use the bot."""
    update.message.reply_text("Нажмите /start чтобы начать")


def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot`s token.
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
