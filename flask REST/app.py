#run this followed by rest_client.py
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/model', methods = ['POST'])
def model_call():
    request_data = request.get_json(force = True)
    model_name = request_data['model']
    return 'You are requesting for a {0} model'.format(model_name)

if __name__ == '__main__':
    app.run()
