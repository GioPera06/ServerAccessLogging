import os
from importlib.machinery import SourceFileLoader

import telegram
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.filters import Filters
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.updater import Updater
from telegram.update import Update

# var = SourceFileLoader("var","/etc/profile.d/var.py").load_module()

TOKEN = os.environ.get('TOKEN')
USER_ID = os.environ.get('USER')
USERNAME = os.environ.get('USERNAME')

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher
bot = telegram.Bot(token=TOKEN)

def closelast(update: Update, context: CallbackContext):
    if (update.message.chat_id == USER_ID and update.message.chat.username == USERNAME) :
        os.system("pkill -9 -t " + var.getSessionId)
    else:
        update.message.reply_text("L'id non corrisponde con quello fornito nel file .env")
        chatidv = update.message.chat_id
        usernamev = update.message.chat.username
        namev = update.message.chat.full_name
        bot.send_message(chat_id = USER_ID, text = namev + "(Username: @" + usernamev + ", ChatId = " + chatidv + ") tryed to kill the last ssh login")

def unknown(update: Update, context: CallbackContext):
	update.message.reply_text(
		"'%s' isn't a known command" % update.message.text)


def unknown_text(update: Update, context: CallbackContext):
	update.message.reply_text("i can't understand '%s'" % update.message.text)

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome user" % update.message.text)

updater.dispatcher.add_handler(CommandHandler('closelast', closelast))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
