from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/string', methods=['GET','POST'])
def get_post_string():
    if request.method == 'POST':
        app_data = request.form
        print('string data, ', app_data)
        return jsonify(app_data)
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
def post_file():
	if request.method == 'POST':
        app_data = request.form
        print('string data, ', app_data)
        return jsonify(app_data)
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
    

@app.route('/json', methods=['GET','POST'])
def pos_post_string():
    if request.method == 'POST':
        json_data = request.get_json()
        print('json data, ', json_data)
        return jsonify(json_data)
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