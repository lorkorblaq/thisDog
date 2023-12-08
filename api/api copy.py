from flask import Flask, render_template, Blueprint
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self, name, test):
        return {"data": name, "test": test}
api.add_resource(HelloWorld, "/helloworld<string:name>")

if __name__ == "__main__":
    app.run(debug=True)