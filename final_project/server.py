from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    if text:
        translator = Translator()
        translation = translator.translate(text, dest='fr')
    return "Translated text to French"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    if text:
        translator = Translator()
        translation = translator.translate(text, dest='eng')
    return "Translated text to English"

@app.route("/")
def renderIndexPage():
    context = {'message': 'Hello, World!'}
    html = render_template('index.html',context)
    return Response(html, content_type='text/html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
