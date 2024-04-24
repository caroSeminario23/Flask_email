#from flask_mail import Mail
from flask import render_template # Importar la función render_template para renderizar plantillas HTML
from flask_mail import Message # Importar la clase Message para crear mensajes de correo electrónico
import correo # Importar el módulo envio.py
from correo import app # Importar la instancia de la aplicación Flask
from correo import mail # Importar la instancia de Mail

@app.route('/send-mail/') # Ruta para enviar un correo electrónico
def send_mail():
    msg = Message("GRUPO 4 - Prueba de envío de correo electrónico", # Asunto del mensaje
                  sender="isaproyectosfisi@gmail.com", # Remitente
                  recipients=["semivaldi@gmail.com"]) # Destinatario
    #mail.send(msg)
    msg.body = "Este es un mensaje enviado por el GRUPO 4 - DSW" # Cuerpo del mensaje
    #mail.send(msg) # Enviar el mensaje

    try: # Manejar errores
        mail.send(msg) # Enviar el mensaje
        return "Mensaje enviado" # Devolver un mensaje de confirmación
    except Exception as e: # Capturar cualquier excepción
        return f"Ha ocurrido un error al enviar el correo electrónico: {str(e)}" # Devolver un mensaje de error

    return "Mensaje enviado" # Devolver un mensaje de confirmación

if __name__ == '__main__': # Si el script se ejecuta directamente
    app.run(host='0.0.0.0', debug=True, port=5000) # Ejecutar la aplicación en modo de depuración