#run this followed by ml_rest_client.py
from flask import Flask, request
import pickle

import numpy as np
local_classifier = pickle.load(open('classifier.pickle','rb'))
local_scaler = pickle.load(open('sc.pickle', 'rb'))

app = Flask(__name__)

@app.route('/predict', methods = ['POST'])
def model_predict():
    request_data = request.get_json(force = True)
    age = request_data['age']
    salary = request_data['salary']
    prediction = local_classifier.predict(local_scaler.transform(np.array([[age, salary]])))
    predProb = local_classifier.predict_proba(local_scaler.transform(np.array([[age, salary]])))
    return 'The prediction is {0} and probablity is {1}'.format(prediction, predProb)

if __name__ == '__main__':
    app.run(port = 8000, debug = True)
