from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
from decouple import config

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my App key'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = config('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = config('MAIL_PASSWORD')


app.config['MAIL_DEFAULT_SENDER'] = config('MAIL_USERNAME')

mail = Mail(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)


@app.route('/')
def index():
    return render_template('main.html')

@app.route('/sendemail/', methods=['POST'])
def send_email():
    # Get form data
    name = request.form['name']
    subject = request.form['Subject']
    email = request.form['_replyto']
    message = request.form['message']

    # Create message
    msg = Message(subject, sender='ogolasospeter62@gmail.com', recipients=['email',])
    msg.body = f"From: {name}\nEmail: {email}\n\n{message}"

    # Send email
    mail.send(msg)

    return 'Email sent successfully!'


