# Configurar Flask-Mail para enviar correos electrónicos desde Gmail
import os
from flask import Flask, app
from flask_mail import Mail

app = Flask(__name__) # Crear una instancia de Flask

app.config['MAIL_SERVER'] = 'smtp.googlemail.com' # Servidor SMTP de Gmail
app.config['MAIL_PORT'] = 587 # Puerto de Gmail
app.config['MAIL_USE_TLS'] = True # Habilitar TLS (Transport Layer Security)
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME') # Evita exponer el nombre de usuario
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD') # Evita exponer la contraseña

mail = Mail(app) # Crear una instancia de Mail