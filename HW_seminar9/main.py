from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters, ConversationHandler
from random import randint
import Functions

# 1) Напишите Бота, удаляющего из текста все слова, содержащие "абв". (Ввод от пользователя)
# 2) Создайте Бота для игры с конфетами человек против бота. (Дополнительно)




app = ApplicationBuilder().token("5801378497:AAGDg-L8eFJNMPsqo57l-kVuXgJ5dmuCpF8").build()

app.add_handler(ConversationHandler(entry_points= [CommandHandler("game", Functions.game)], 
                                    states={Functions.my_turn:[MessageHandler(filters.TEXT, Functions.gamer_turn)], 
                                           Functions.bot:[MessageHandler(filters.TEXT, Functions.bot_turn)]},
                                    fallbacks=[CommandHandler("cancel", Functions.cancel)]))

app.add_handler(CommandHandler("hello", Functions.hello))
app.add_handler(MessageHandler(filters.TEXT, Functions.del_word))


app.run_polling()