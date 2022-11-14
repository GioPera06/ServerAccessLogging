import subprocess
import os
import telegram
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.filters import Filters
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.updater import Updater
from telegram.update import Update

USER_ID = os.environ.get('USER')
TOKEN = os.environ.get('TOKEN')
bot = telegram.Bot(token=TOKEN)

def main():

    hostname = subprocess.run("hostname")
    login_ip = subprocess.run("echo $SSH_CONNECTION | cut -d " " -f 1")
    login_date = subprocess.run('date')
    login_name = subprocess.run("whoami")
    session_id = subprocess.run('echo "$(tty | sed -e ''s:/dev/::'')"')

    if ('cat /var/log/auth.log | egrep ''^.*?\bpublickey\b.*?\b'" + login_ip + '"'\b.*?$'''):
      method = "Public Key Authentication"
    else:
      method="Password(or generic) Authentication"

    
    bot.send_message(chat_id = USER_ID, text = 'telegram-send "📲 New Server Login (' + hostname + ') \n Logged User: ' + login_name +'\n IP-Address: '+ login_ip +'\nDate: ' + login_date + '\nSession: ' + session_id + ' \nMethod: ' + method +' \n\nUse: "pkill -9 -t ' + session_id + '" to kill that session"')

if __name__ == '__main__':
    main()