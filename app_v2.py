from flask import Flask, render_template, request
import numpy as np
import pickle
import joblib
import os

app = Flask(__name__, template_folder='templates', static_folder='static')
filename = 'wine_dt.pkl'

# load the scaler and model from the PKL file
with open(filename, 'rb') as f:
    scaler, model = pickle.load(f)

@app.route('/predict', methods=['POST'])

def index():
    return render_template('index.html')


def predict():
    alcohol = request.form['alcohol']
    sulphates = request.form['sulphates']
    citric_acid = request.form['citric_acid']
    volatile_acidity = request.form['volatile_acidity']

    data = np.array([[alcohol, sulphates, 
                      citric_acid, volatile_acidity]], 
                      dtype=float)
    
    # Scale data for model
    data = scaler.transform(data)
    
    # Make Predictions
    pred = model.predict(data)

    return render_template('index.html', predict=str(pred))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
