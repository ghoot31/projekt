# app.py - a minimal flask api using flask_restful
from flask import Flask
from flask_restful import Resource, Api
from flask import request
import string

app = Flask(__name__)
api = Api(app)

class Pokemon(Resource):
    def post(self):
        text = request.form['text']
        caps = False
        poke_text = ''
        for char in text:
            if char in string.ascii_letters:
                if caps:
                    char = char.upper()
                else:
                    char = char.lower()
            poke_text += char
            caps = not caps

        return {'text': poke_text}

api.add_resource(Pokemon, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
