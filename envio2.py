#from flask import render_template # Importar la función render_template para renderizar plantillas HTML
from flask_mail import Message # Importar la clase Message para crear mensajes de correo electrónico
from correo import app, mail # Importar la instancia de la aplicación Flask
from threading import Thread

def send_async_email(app, msg):
    with app.app_context(): # Crear un contexto de aplicación para trabajar con Flask-Mail
        mail.send(msg) # Enviar el correo electrónico utilizando la instancia de Mail

@app.route('/send-mail/') # Ruta para enviar un correo electrónico
def send_mail_route():
    to = "daryel.16.09@gmail.com"
    subject = "Prueba de envío de correo electrónico"
    body = "Este es un correo de prueba, que grantiza la creacion de un hilo que permite al programa continuar ejecutándose sin esperar a que se complete el envío del correo electrónico "
    result = send_mail(to, subject, body)
    return result

def send_mail(to, subject, body, ):
    msg = Message("GRUPO 4 "+subject, # Asunto del mensaje
                  sender=app.config["MAIL_USERNAME"], # Remitente
                  recipients=[to]) # Destinatario
    msg.body = body # Cuerpo del mensaje
    thr = Thread(target=send_async_email, args=[app, msg]) # Crear un hilo con la función y los argumentos necesarios
    thr.start() # Iniciar el hilo para enviar el correo electrónico
    return "Correo enviado correctamente" # Devolver un mensaje de confirmación

if __name__ == '__main__': # Si el script se ejecuta directamente
    app.run(host='0.0.0.0', debug=True, port=5000) # Ejecutar la aplicación en modo de depuración