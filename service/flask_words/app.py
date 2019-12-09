from flask import Flask
from flask_restful import Resource, Api
from flask import request
import regex
import string

app = Flask(__name__)
api = Api(app)


class Words(Resource):
    def post(self):
        text = regex.sub(u"\\p{P}+", "", request.form['text'])
        all_words = {}
        for word in text.split():
            word = word.lower()
            if word not in all_words.keys():
                all_words[word] = 1
            else:
                all_words[word] += 1

        return_string = ''
        for word in sorted(all_words.items()):
            return_string += str(word[0]) + "- " + str(word[1]) + "\n"
        return {'text': return_string}


api.add_resource(Words, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
