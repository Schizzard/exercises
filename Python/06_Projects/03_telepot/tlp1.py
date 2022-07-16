from pprint import pprint
import telepot

from telepot.loop import MessageLoop


token = '5017969562:AAGZtaIlwmzCzaO4bpEUvCl5PL6dpJ6ZsfE'
bot = telepot.Bot(token)
# bot.getMe()
bot.deleteWebhook()
response = bot.getUpdates(546727470)
pprint(response)

def handle(msg):
    pprint(msg)
    print()

MessageLoop(bot, handle).run_as_thread()


bot.sendMessage(392350805, 'Hey!')