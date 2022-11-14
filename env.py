import subprocess
import os

os.environ["TOKEN"] = input("Insert you're bot token: ")
os.environ["USER"] = input("Insert you're username id: ")


subprocess.run('chmod +x telegram-send.sh')

subprocess.run('sudo cp telegram-send.sh /usr/bin/telegram-send')
subprocess.run('sudo chown root:root /usr/bin/telegram-send')

subprocess.run('mkdir -p /var/serveraccesslogging')
subprocess.run('  sudo cp .env /var/serveraccesslogging/.env.local')

subprocess.run('  sudo cp message.txt /var/serveraccesslogging/message.txt')

subprocess.run('sudo cp bot.py /var/serveraccesslogging/bot.py')

subprocess.run('sudo cp access-notify.sh /etc/profile.d/access-notify.sh')

subprocess.run('sudo cp var.py /etc/profile.d/var.py')

print("Completed! Now the file .env.local is in this folder: /var/serveraccesslogging/.env.local, and you can customize the message in the same folder but in the file message.txt")