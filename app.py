from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
from io import StringIO
import json

import numpy as np
import pandas as pd
#import seaborn as sn
#import matplotlib.pyplot as plt
#plt.sytle.use('ggplot')

from sklearn.datasets import load_boston, load_iris, load_wine

from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV

from sklearn import linear_model

from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.linear_model import LogisticRegression

from sklearn.svm import SVC

from sklearn.metrics import mean_squared_error
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from sklearn.metrics import accuracy_score

from sklearn.pipeline import Pipeline

from sklearn.preprocessing import Imputer
from sklearn.preprocessing import StandardScaler

boston = load_boston()
wine = load_wine()
iris = load_iris()

app = Flask(__name__)
CORS(app)

def Logistic_regression(data):

	df = pd.read_csv(data)

	X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
	y = df['species']
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3,random_state=5)
		
	scaler = StandardScaler()
	X_train_scaled = scaler.fit_transform(X_train)
	X_test_scaled = scaler.transform(X_test)
		
	c_logspace = np.logspace(-2, 2, 30)
	model = LogisticRegression()
	param_grid ={'C': c_logspace,'penalty': ['l1', 'l2']}
	model_cv = GridSearchCV(model, param_grid, cv=5)
	model_cv.fit(X_train_scaled, y_train)
	y_pred = model_cv.predict(X_test_scaled)
	
	score_train = model_cv.score(X_train_scaled, y_train)
	score_test = model_cv.score(X_test_scaled, y_test)
	best_params = model_cv.best_params_	
	con_matrix = confusion_matrix(y_test, y_pred)
	report = classification_report(y_test, y_pred)
	
	return {'trainingScore': score_train, 'testingScore': score_test, 'bestParams':best_params,'report': report} #'confusionMatrix': con_matrix, }
	#return score_train, score_test, best_params, con_matrix, report

@app.route('/ml', methods=['GET', 'POST', 'OPTIONS'])
def ml():
	if request.method == 'POST':
		incoming_data = request.data
		#print('incoming data, ', incoming_data)
		data_received = json.loads(incoming_data)
		# print('data_data dictionary', data_received)
		# print('type: ', type(data_received))

		testData = StringIO(data_received)
		results = Logistic_regression(testData)
		#score_train, score_test, best_params, confusion_matrix, classificaiton_report
		
		#print('logistic regression results data type:', type(results))
		#print('Accuracy of Logistic regression classifier on training set: {:.2f}'.format(results[0]))
		#print('Accuracy of Logistic regression classifier on test set: {:.2f}'.format(results[1]))
		#print("Tuned Model Parameter: {}".format(results[2]))
		#print('confusion matrix: ', results[3])
		#print('classification report: ', results[4])
		
		print ('results type = ', type(results))		
		return jsonify(results)
	else:
		return jsonify('something broke')

@app.route('/data', methods=['GET','POST'])
def data_test():
	if request.method == 'POST':
		data_data = request.data
		print('data data, ', data_data)
		d = json.loads(data_data)
		print('data_data dictionary', d)
		print('type: ', type(d))
		
		testData = StringIO(d)

		df = pd.read_csv(testData)

		print('df = ', df)
		
		
		# d is a string, return jsonified string
		return jsonify(d)
	else:
		dic = {"language": "python",
	            "framework": "Flask",
	            "name": "Zach",
	            "v": {
		                "p" : 3.4,
		                "f" : 12
	             },
	            "examples" : ["hi", "hello"],
	            "boolean_test" : 'true',
	
	            }
		return jsonify(dic)

@app.route('/form', methods=['GET','POST'])
def form():
    if request.method == 'POST':
        form_data = request.form
        print('form data, ', form_data)
        return jsonify(form_data)
    else:
        dic = {"language": "python",
	            "framework": "Flask",
	            "name": "Zach",
	            "v": {
		                "p" : 3.4,
		                "f" : 12
	             },
	            "examples" : ["hi", "hello"],
	            "boolean_test" : 'true',
	
	            }
        return jsonify(dic)

@app.route('/file', methods=['GET','POST'])
def file_data():	
	if request.method == 'POST':
		file_data = request.file
		print('string data, ', file_data)
		print(type(file_data))
		return jsonify('hello files')
	else:
		dic = {"language": "python",
	            "framework": "Flask",
	            "name": "Zach",
	            "v": {
		                "p" : 3.4,
		                "f" : 12
	             },
	            "examples" : ["hi", "hello"],
	            "boolean_test" : 'true',
	
	            }
		return jsonify(dic)

@app.route('/json', methods=['GET','POST','OPTIONS'])
def json_data():
	if request.method == 'POST':
		print('request is POST')
		test_json_data = request.get_json()
		print('test_json_data: ', test_json_data)
		d = json.loads(test_json_data)
		print('json data: ', d)
		return 'No Data Received'
	
	else:
		dic = {"language": "python",
	            "framework": "Flask",
	            "name": "Zach",
	            "v": {
		                "p" : 3.4,
		                "f" : 12
	             },
	            "examples" : ["hi", "hello"],
	            "boolean_test" : 'true',
	
	            }
		return jsonify(dic)
        
if __name__ == '__main__':
    app.run(debug=True, port=5000)
    
