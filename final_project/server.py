from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")
logged = []

@app.route("/englishToFrench")
def translateToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translated = translator.translateToFrench(textToTranslate)
    logged.append({"mode": "en-fr", "input": textToTranslate, "output": translated})
    return "%s translated into %s" %(textToTranslate, translated)

@app.route("/frenchToEnglish")
def translateToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translated = translator.translateToEnglish(textToTranslate)
    logged.append({"mode": "fr-en", "input": textToTranslate, "output": translated})
    return "%s translated into %s" %(textToTranslate, translated)

@app.route("/")
def renderIndexPage():
    return json.dumps(logged)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
