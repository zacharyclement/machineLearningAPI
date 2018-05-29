from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

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

@app.route('/data', methods=['GET','POST'])
def data():
	if request.method == 'POST':
		data_data = request.data
		print('data data, ', data_data)
		d = json.loads(data_data)
		print('data_data dictionary', d)
		print('type: ', type(d))
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
        

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    