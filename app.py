import numpy as np
from joblib import load
from flask import Flask, request, jsonify

#create framework
app = Flask(__name__)

#create simple API
@app.route('/predict', methods=['GET'])
#define method
def get_prediction():
    #load predefined model
    model = load('model.joblib')

    #define features
    sepal_length = float(request.args.get('sl'))
    petal_length = float(request.args.get('pl'))
    features = [[sepal_length, petal_length]]

    #generate predictions
    predicted_class = model.predict(features)

    #change type and return results
    predicted_class = float(predicted_class)
    return jsonify(features=str(features), predicted_class=str(predicted_class))


if __name__ == '__main__':
    #run app at localhost
    app.run(debug=True)

