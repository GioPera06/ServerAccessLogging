# pylint: disable=subprocess-run-check
import subprocess
from getpass import getpass

f = open("./.env", "a", encoding="utf-8")
User = input("Insert the users telegram ID in the format id:id:id:id: ")
f.write("TOKEN=""" + getpass('Insert the bot token here (The input is masked): ') + '"')


subprocess.run('chmod +x telegram-send.sh')

subprocess.run('sudo cp telegram-send.sh /usr/bin/telegram-send')
subprocess.run('sudo chown root:root /usr/bin/telegram-send')

subprocess.run('mkdir -p /var/serveraccesslogging')
subprocess.run('sudo cp .env /var/serveraccesslogging/.env.local')

subprocess.run('sudo cp message.txt /var/serveraccesslogging/message.txt')

subprocess.run('sudo cp bot.py /var/serveraccesslogging/bot.py')

subprocess.run('sudo cp notify.py /etc/profile.d/notify.py')

subprocess.run('sudo cp var.py /etc/profile.d/var.py')

print("\nCompleted! Now the file .env.local is in this folder: /var/serveraccesslogging/.env.local, and you can customize the message in the same folder but in the file message.txt")