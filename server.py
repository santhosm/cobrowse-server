from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import json
import requests
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
api = Api(app)


class intentListener(Resource):
    def post(self):
        res = request.data
        intents = open('intent.json')
        cobrowse = json.load(intents)
        for key, value in cobrowse.items():
            for idx in value:
                print(idx["Conditions"])
                print("***")
                print (eval(res))
                if (idx["Conditions"] == eval(res)):
                    print("$$$$")
                    print(jsonify(idx["Steps"]))
                    return jsonify(idx["Steps"])
            return eval(res)


api.add_resource(intentListener, '/intents')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8180')
