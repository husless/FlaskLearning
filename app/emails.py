from flask.ext.mail import Message
from app import mail
from flask import render_template
from config import ADMINS

from decorators import async

@async
def send_async_email(msg):
    mail.send(msg)


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body, msg.html = text_body, html_body
    send_async_email(msg)

def follower_notification(followed, follower):
    send_email('[microblog] {} is now following you!'.format(follower.nickname),
            ADMINS[0], [followed.email],
            render_template('follower_email.txt', user=followed, follower=follower),
            render_template('follower_email.html', user=followed, follower=follower))
