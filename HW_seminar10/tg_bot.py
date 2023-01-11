from telegram import Bot
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import calculator
import re

TOKEN = ""

bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Введите выражение: ")

def calc(update, context):
    eq = update.message.text
    eq = calculator.split(eq)
    eq = calculator.calculate(eq)
    context.bot.send_message(update.effective_chat.id, *eq)


start_handler = CommandHandler('start', start)
calc_handler = MessageHandler(Filters.text, calc)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(calc_handler)


updater.start_polling()
updater.idle()