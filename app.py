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
    return render_template("home.html")

@app.route('/send_message', methods=['GET', 'POST'])
def send_message():
    if request.method == "POST":
        email = request.form['email']
        subject = request.form['subject']
        message_body = request.form['message_body']

        send_email(email, subject, 'template', message_body=message_body)

        success = "Message sent"
        return render_template("result.html", email=email, success=success)

if __name__ == "__main__":
    app.run(debug=True)