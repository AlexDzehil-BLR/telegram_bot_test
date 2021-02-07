import logging
from telegram.ext import Updater, CommandHandler

logging.basicConfig(filename='bot.log', level=logging.INFO)

def greet_user(update, context):
    print('Вызван /start')
    print(1/0)
    update.message.reply_text(update)

def main():
    mybot = Updater("1618613141:AAHWGYgMfWBDTyPjpTZ4IiTdXl7kzDXvMzA", use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))

    logging.info('Bot started')
    mybot.start_polling()
    mybot.idle()

main()