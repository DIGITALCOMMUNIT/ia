# Importamos las librerías que necesitaremos
from flask import Flask, render_template, request
import nltk

# Creamos una instancia de la clase Flask y definimos una ruta para la página principal
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Definimos una ruta para enviar preguntas a la IA y recibir respuestas
@app.route('/pregunta', methods=['POST'])
def pregunta():
    # Recibimos la pregunta del usuario
    pregunta = request.form['pregunta']

    # Procesamos la pregunta y encontramos la respuesta más adecuada utilizando NLTK
    tokens = nltk.word_tokenize(pregunta)
    classifier = nltk.MaxentClassifier.train(train, 'lbfgs', trace=0, max_iter=1000)
    respuesta = classifier.classify(dict((word, True) for word in tokens))

    # Devolvemos la respuesta al usuario
    return respuesta

if __name__ == '__main__':
    app.run()
