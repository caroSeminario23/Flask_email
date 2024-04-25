import os
from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = True
app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
app.config['FLASKY_MAIL_SENDER'] = 'davidfernandezdavila01@gmail.com'
app.config['FLASKY_ADMIN'] =os.environ.get('FLASKY_ADMIN')

mail = Mail(app)

def send_email(to, subject, template, **kwargs):
    message = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
                      sender=app.config['FLASKY_MAIL_SENDER'],
                      recipients=[to])
    message.html = render_template(template + '.html', **kwargs)
    message.body = render_template(template + '.txt', **kwargs)
    mail.send(message)

@app.route('/')
def index():
    return render_template("homeUser.html")

@app.route('/send_message', methods=['GET', 'POST'])
def send_message():
    if request.method == "POST":
        user=request.form['user']
        email = request.form['email']
        message_body = request.form['message_body']

        send_email(app.config['FLASKY_ADMIN'], 'User New', 'templateUser', user=user, email=email,message_body=message_body)

        success = "Registered user and Message sent"
        return render_template("resultUser.html", admin=app.config['FLASKY_ADMIN'], success=success)

if __name__ == "__main__":
    app.run(debug=True)