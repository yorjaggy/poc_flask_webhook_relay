from flask import Flask
from flask import request
import json
import random

app = Flask(__name__)

x = {
    1: "¿Qué es una respuesta no autoritativa y quién emite esta respuesta?",
    2: "Explique los 3 componentes del sistema DNS",
    3: "¿Qué configuraciones permite obtener el DHCP?",
    4: "Enumere 4 tipos de registros DNS y explique para qué sirve",
    5: "¿Qué es SOA?",
    6: "Explique en cuantos pasos y como podria resolverse el nombre de dominio www.icesi.edu.co",
    7: '<p>Pepito escribe www.icesi.edu.co en la barra del navegador y en su pantalla aparece la p&aacute;gina de un banco en Berl&iacute;n. Analice los registros DNS indicados y explique porqu&eacute; sucedi&oacute; el error a Pepito.</p><p>Registros DNS:</p><table style="margin-left: auto; margin-right: auto;"><tbody><tr><td>A =</td><td>190.234.17.200</td></tr><tr><td>MX =</td><td>172.10.15.255</td></tr></tbody></table><p>&nbsp;</p><p><img src="http://i2thub.icesi.edu.co:9992/guaralrpc/Screenshot%20from%202019-11-01%2010-56-48.png" alt="" width="446" height="244" /></p>',  8: "Su amigo pedro montó un servidor DNS en su casa y actualiza los registros para que la ip privada de pedro responda al nombre www.elmundomagicodelestudiante.com. Le pide a usted que consulte el sitio web, pero no le fue posible. Expliquele a pedro por que no funciono.",
    9: "¿Qué es SMTP?",
    10: "¿Cuántos servidores DNS root existen y cuál es la tarea de estos servidores?"}

@app.route("/")
def hello():
    # To extract params from url
    #parm = request.args.get('num')
    #return x[int(parm)]
    
    question = random.randrange(1,10)
    return x[question]


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=8585)