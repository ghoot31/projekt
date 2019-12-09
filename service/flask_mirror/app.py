# app.py - a minimal flask api using flask_restful
from flask import Flask
from flask_restful import Resource, Api
from flask import request

app = Flask(__name__)
api = Api(app)


class Mirror(Resource):
    def post(self):
        text = request.form['text']
        return {'text': text[::-1]}


api.add_resource(Mirror, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
