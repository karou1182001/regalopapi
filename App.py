#Se le puede agregar un cronometro, y que se suba a internet
#Librerías
import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
import flask
import numpy as np
import pyautogui as pg
import webbrowser as web
from time import sleep
from numpy.lib.function_base import select
from typing import Text
from gtts import gTTS
from playsound import playsound
from os import remove
import speech_recognition as sr
import os
import pywhatkit

app = Flask(__name__)


#Iniciar una sesión
#app.secret_key='mysecretkey'

###NUEVA APP##
#FUNCIONES
def audio(frase):
    print(frase)
    audio= "speech.mp3"
    if os.path.exists(audio):
        remove(audio)
    language= "es"
    sp= gTTS(text= frase, lang= language, slow= False)
    sp.save(audio)
    playsound(audio)



@app.route('/') #Decorador que indica que cada vez que un user entre a la ruta principal de la app se le devolverá una respuesta.
def index():
    return render_template('index.html')

#Carta de presentación
@app.route("/presentacion")
def presentacion(): 
    frase="Querido Emilio Zapata, necesitamos lea esto urgente"
    audio(frase)
    return render_template("presentacion.html")

@app.route("/ingresopc")
def ingresopc(): 
    return render_template("ingresopc.html")

@app.route("/ingresar_ingresopc", methods=["POST"])
def ingresar_ingresopc(): 
    if request.method == "POST":
        password = request.form["password"]
        if password== "0,1,1,2,3,5,8,13,21,34,55,89":
            return render_template("acertijo2.html")
        else:
          flash("Contraseña incorrecta")
          return redirect(url_for("ingresopc"))  

#ACERTIJO2
@app.route("/acertijo2")
def acertijo2(): 
    return render_template("acertijo2.html")

@app.route("/respuesta_a2", methods=["POST"])
def respuesta_a2(): 
    if request.method == "POST":
        password = request.form["password"]
        if "hijo"in password:
            return render_template("acertijo3.html")
        else:
            flash("Contraseña incorrecta")
            return redirect(url_for("acertijo2")) 

#ACERTIJO3
@app.route("/acertijo3")
def acertijo3(): 
    return render_template("acertijo3.html")

@app.route("/spam", methods=["POST"])
def spam(): 
    if request.method == "POST":
       tel = request.form["tel"]
       tel= "+57" + tel
       tel= "https://web.whatsapp.com/send?phone= " + tel
       web.open(tel)
       #Este sleep es para dejar cargar la página de whatsapp
       sleep(10)
       for i in range(21):
            if i==0:
                pg.typewrite("--HACIENDO SPAM--")
                pg.press("enter")
            if i == 1:
                pg.typewrite("Antes de ayer,")
                pg.press("enter")
            elif i==8:
                pg.typewrite("Julia tenía 15 años. El año que viene, ")
                pg.press("enter")
            elif i==11:
                pg.typewrite("tendrá 18.")
                pg.press("enter")   
            elif i==20:
                pg.typewrite("¿Qué día es hoy?")
                pg.press("enter") 
            elif i==5 or i==9 or i==15:
                pg.typewrite("¿Qué se puede encontrar una vez en un minuto")
                pg.press("enter") 
            elif i== 4 or i==10 or i==12:
                pg.typewrite("dos veces en un momento y nunca en cien años?")
                pg.press("enter") 
            else:
                pg.typewrite("Misterio cantando una canción.")
                pg.press("enter")
            
     
       return render_template("acertijo3.html")

@app.route("/respuesta_a3", methods=["POST"])
def respuesta_a3(): 
    if request.method == "POST":
        password = request.form["password"]
        if "1 de enero"in password:
            return render_template("acertijo4.html")
        else:
            flash("Contraseña incorrecta")
            return redirect(url_for("acertijo3")) 
#ACERTIJO4
@app.route("/acertijo4")
def acertijo4(): 
    return render_template("acertijo4.html")

#ACERTIJO5
@app.route("/acertijo5", methods=["POST"])
def acertijo5(): 
    return render_template("acertijo5.html")

@app.route("/respuesta_a5", methods=["POST"])
def respuesta_a5(): 
    if request.method == "POST":
        password = request.form["password"]
        if  password== "1837392":
            return render_template("acertijo6.html")
        else:
            flash("Contraseña incorrecta")
            return redirect(url_for("acertijo5")) 
#ACERTIJO6
@app.route("/acertijo6")
def acertijo6(): 
    return render_template("acertijo6.html")

@app.route("/met", methods=["POST"])
def met():
    audio("Buenas. Yo soy Alexa. Tiene que hallar qué palabra dice en el minuto uno con cero cinco la canción Tu poeta")
    music="Tu poeta"
    audio('Reproduciendo ' + music)
    pywhatkit.playonyt(music)
    return render_template("acertijo6.html")

@app.route("/respuesta_a6", methods=["POST"])
def respuesta_a6(): 
    if request.method == "POST":
        password = request.form["password"]
        if "princesa" in password or "mi" in password:
            return render_template("acertijo7.html")
        else:
            flash("Contraseña incorrecta")
            return redirect(url_for("acertijo6")) 
   

#ACERTIJO7
@app.route("/acertijo7", methods=["POST"])
def acertijo7(): 
    return render_template("acertijo7.html")

@app.route("/respuesta_a7", methods=["POST"])
def respuesta_a7(): 
    if request.method == "POST":
        password = request.form["password"]
        if "trasnocharse" in password:
            return render_template("acertijo8.html")
        else:
            flash("Contraseña incorrecta")
            return redirect(url_for("acertijo7")) 

#ACERTIJO8
@app.route("/acertijo8", methods=["POST"])
def acertijo8(): 
    return render_template("acertijo8.html")

@app.route("/respuesta_a8", methods=["POST"])
def respuesta_a8(): 
    if request.method == "POST":
        password = request.form["password"]
        if "tiktok" in password:
            return render_template("acertijo9.html")
        else:
            flash("Contraseña incorrecta")
            return redirect(url_for("acertijo8")) 
    
#ACERTIJO9
@app.route("/acertijo9", methods=["POST"])
def acertijo9(): 
    return render_template("acertijo9.html")

@app.route("/respuesta_a9", methods=["POST"])
def respuesta_a9(): 
    if request.method == "POST":
        password = request.form["password"]
        if "pa" in password:
            music="seven years"
            audio('¡Lo ha logrado!')
            pywhatkit.playonyt(music)
            return render_template("final.html")
        else:
            flash("Contraseña incorrecta")
            return redirect(url_for("acertijo9")) 



#Se conecta por el puerto 3000
if __name__ == '__main__':
    app.run(port = 3000, debug=True)
