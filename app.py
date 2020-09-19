import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict',methods=['POST'])
def predict():
	label = ""
	sepallength = request.form["sepallength"]
	sepalwidth = request.form["sepalwidth"]
	petallength = request.form["petallength"]
	petalwidth =request.form["petallength"]
	int_features = [sepallength,sepalwidth , petallength ,petalwidth]
	
	final_features = [np.array(int_features)]
	prediction = model.predict(final_features)[0]
	if prediction == 0 :
		label = "Iris-virginica"
	elif prediction == 1:
		label = "Iris-versicolor"
	else:
		label = "Iris-setosa"
		
	return render_template('index.html', prediction_text='Predicted Flower should be $ {}'.format(label))


if __name__ == "__main__":
    app.run(debug=True)