import os

hostname = os.system("hostname")
login_ip = os.system('echo $SSH_CONNECTION | cut -d " " -f 1')
login_date = os.system('date +"%A %e %b %Y -  %d\/%m\/%y - %r"')
login_name = os.system('whoami')
session_id = os.system("echo tty | sed -e 's:/dev/::'")

def getHostname:
    return hostname

def getLoginDate:
    return login_ip

def getLoginIp:
    return login_date

def getLoginName:
    return login_name

def gestSessionId:
    return session_id
