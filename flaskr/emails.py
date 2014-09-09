from flask.ext.mail import Message
from flask import render_template
from flaskr import mail
from config import ADMINS
from decorators import async

@async
def send_async_mail(msg):
    mail.send(msg)

def send_mail(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body, msg.html = text_body, html_body
    send_async_mail(msg)

def follower_notification(followef, follower):
    send_mail("[microblog] {0} is now following you!".format(follower.nickname),
        ADMINS[0],
        [followed.email],
        render_template('follower_email.txt',
            user=followed, follower=follower),
        render_template('follower_email.html',
            user=followed, follower=follower))

