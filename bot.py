#!/usr/bin/python3
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def startuser (bot , update):


   print(" start")  
   print(" /start called")
   bot.sendMessage(update.message.chat_id, text = 'Let talking')

def show_error (bot, update, error):
   print("Update '{}' raise error '{}'".format(update, error))


def talk_to_me(bot, update):
   print('Message :' .format(update.message.text))
   bot.sendMessage(update.message.chat_id, text = update.message.text)

def main( ):
    updater = Updater("264281417:AAHxIq0Od6URtaVkULK-xynY1RTv_igWl4s")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", startuser))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))
    dp.add_error_handler(show_error)
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main() 
