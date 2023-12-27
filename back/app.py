from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_restful import Resource
from flask import send_file

app = Flask(__name__)
CORS(app)
api = Api(app)

#图片放这里
@app.route('/image')
def get_image():
    return send_file('1.png', mimetype='image/png')
@app.route('/image2')
def get_image2():
    return send_file('2.png', mimetype='image/png')



def index():
    return "Welcome to API v1, try /hello."


class Hello(Resource):
    @staticmethod
    def get():
        return "[get] hello flask"

    @staticmethod
    def post():
        return "[post] hello flask"


api.add_resource(Hello, '/hello')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8010)
