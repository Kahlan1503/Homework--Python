from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters, ConversationHandler
from random import randint

total_candy = 120
my_turn = 0
bot = 1


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def del_word(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    data = list(filter(lambda x: 'абв' not in x, text.split()))
    await update.message.reply_text(f'{" ".join(data)}')

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Так и не доиграли, пока!')

async def game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global total_candy
    await update.message.reply_text(f'Начнем игру! \nНа столе лежит {total_candy} конфет.\nХод Игрока. Какое количесвто конфет взять:')   
    return my_turn


async def gamer_turn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global total_candy
    player = int(update.message.text)
    if total_candy == 0:
        await update.message.reply_text('Игрок победил!')
        return
    elif 0 < player < 29:
        total_candy -= player
        await update.message.reply_text(f'На столе осталось {total_candy} конфет.')
        return bot
    else:
        await update.message.reply_text('Вы не можете взять столько конфет.\nКакое количесвто конфет взять:')
        return my_turn
    


async def bot_turn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global total_candy

    if total_candy <= 28:
        await update.message.reply_text(f'БОТ забирает последние конфеты и выигрывает!')
        return
    else: 
        bot_take = total_candy % 29
        if bot_take == 0:
            bot_take = randint(1,28)
        total_candy -= bot_take
        await update.message.reply_text(f'БОТ взял {bot_take} конфет\nНа столе осталось {total_candy} конфет.')
        return my_turn