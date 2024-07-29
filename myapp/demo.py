from flask import Flask, request

app = Flask(__name__)

# Routes
@app.route('/')
def index():
    return "Happy Coding!"

@app.route('/post', methods = ['POST'])
def process_request():
    json = request.json
    print(json)
    return json

if __name__ == '__main__':
    app.run(debug=True)