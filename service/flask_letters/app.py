from flask import Flask
from flask_restful import Resource, Api
from flask import request
import regex

app = Flask(__name__)
api = Api(app)


class Letters(Resource):
    def post(self):
        text = regex.sub(u"\\p{P}+", "", request.form['text'])
        all_chars = {}
        for char in text:
            if char not in all_chars.keys():
                all_chars[char] = 1
            else:
                all_chars[char] += 1

        return_string = ''
        for char in sorted(all_chars.items()):
            return_string += str(char[0]) + ": " + str(char[1]) + "\n"
        return {'text': return_string}


api.add_resource(Letters, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
