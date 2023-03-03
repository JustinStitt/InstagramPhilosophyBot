import sys
import json
import base64
from io import BytesIO
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS

from philQuotes import Creator

application = Flask(__name__)
CORS(application, resources={r"*": {"origins": "*"}})
api = Api(application)


class HelloWorld(Resource):
    def get(self):
        return {"Hello": "Philosophy"}


class GetImage(Resource):
    def get(self):
        creator = Creator()
        content = creator.generateContent()  # returns PIL jpeg
        buffered = BytesIO()
        content.save(buffered, format="JPEG")
        content_base64 = base64.b64encode(buffered.getvalue())
        response = jsonify(
            {"message": "request made", "content": content_base64.decode("utf-8")}
        )
        return response
        # return {"Hello": " philosophy api!"}


api.add_resource(GetImage, "/getimage")
api.add_resource(HelloWorld, "/")

if __name__ == "__main__":
    # application.debug = True
    application.run()
