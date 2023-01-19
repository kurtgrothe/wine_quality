from flask import Flask, render_template, request
import numpy as np
import pickle
import joblib
app = Flask(__name__, template_folder='templates', static_folder='static')
filename = 'dt.pkl'
#model = pickle.load(open(filename, 'rb'))
model = joblib.load(filename)
#model = joblib.load(filename)
@app.route('/')


def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])

def predict():
    alcohol = request.form['alcohol']
    writing_score = request.form['sulphates']
    citric_acid = request.form['citric_acid']
    volatile_acidity = request.form['volatile_acidity']


    pred = model.predict(np.array([[alcohol, sulphates,
                                    citric_acid, volatile_acidity]], dtype=float))

    return render_template('index.html', predict=str(pred))

if __name__ == '__main__':
    app.run
