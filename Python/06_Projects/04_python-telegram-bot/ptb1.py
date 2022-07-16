import telegram
from pprint import pprint


TOKEN = '5017969562:AAGZtaIlwmzCzaO4bpEUvCl5PL6dpJ6ZsfE'
bot = telegram.Bot(token=TOKEN)
print(bot.get_me())

updates = bot.get_updates()

print(updates[0])

bot.send_message(text='Hi Johny!', chat_id=392350805)

