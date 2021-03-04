from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from handlers import greet_user, guess_number, send_cat_picture, user_coordinats, talk_to_me
import logging
import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)

def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('guess', guess_number))
    dp.add_handler(CommandHandler('cat', send_cat_picture))
    dp.add_handler(MessageHandler(Filters.regex('^(Прислать Чувака)$'), send_cat_picture))
    dp.add_handler(MessageHandler(Filters.location, user_coordinats))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Bot started')
    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()