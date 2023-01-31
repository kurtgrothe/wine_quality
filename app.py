from flask import Flask, render_template, request
import numpy as np
import pickle
import joblib
import os

app = Flask(__name__, template_folder='templates', static_folder='static')
filename = 'wine_dt.pkl'
#model = pickle.load(open(filename, 'rb'))
model = joblib.load(filename)

@app.route('/')


def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])

def predict():
    alcohol = request.form['alcohol']
    sulphates = request.form['sulphates']
    citric_acid = request.form['citric_acid']
    volatile_acidity = request.form['volatile_acidity']

 
    pred = model.predict(np.array([[alcohol, sulphates, citric_acid, volatile_acidity]], dtype=float))

    return render_template('index.html', predict=str(pred))

# if __name__ == '__main__':
#     app.run

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
