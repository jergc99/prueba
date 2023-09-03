from threading import Thread
from flask import render_template
from flask_mail import Message


def send_confirmation_email(email):
    from main import app, mail

    msg = Message(
        subject="Confirmation mail",
        sender=app.config["MAIL_USERNAME"],
        recipients=[email],
    )
    msg.html = render_template("sign_in_confirmation_email.html")

    def send_email_async(msg):
        with app.app_context():
            mail.send(msg)

    thread = Thread(target=send_email_async, args=(msg,))
    thread.start()


def send_password_email(email, username, password):
    from main import app, mail

    msg = Message(
        subject="Password recovery",
        sender=app.config["MAIL_USERNAME"],
        recipients=[email],
    )
    msg.html = render_template(
        "password_recovery.html", username=username, password=password
    )

    def send_email_async(msg):
        with app.app_context():
            mail.send(msg)

    thread = Thread(target=send_email_async, args=(msg,))
    thread.start()
