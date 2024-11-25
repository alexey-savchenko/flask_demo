from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

@app.route('/validate', methods = ['POST'])
def process_request():
    pipe = pipeline("text-classification", model="eliasalbouzidi/distilroberta-nsfw-text-classifier")

    json = request.json

    prompt = json.get('prompt')

    if prompt != '':
        validationResult = pipe(prompt)
        validationLabel = validationResult[0]['label']
        return jsonify(
            result=validationLabel
        )
    else:
        return jsonify(
            result='invalid_input'
        )

@app.route('/test', methods = ['GET'])
def test_route():
    return jsonify(
        result='its running'
    )

if __name__ == '__main__':
    app.run(debug=True)