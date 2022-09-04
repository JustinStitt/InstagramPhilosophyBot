import sys
import json
import base64
from io import BytesIO
import numpy as np
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from philQuotes import Creator

app = Flask(__name__)
api = Api(app)


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
        # json_data = json.dumps(np.array(content).tolist())
        # new_image = Image.fromarray(np.array(json.loads(json_data), dtype="uint8"))
        response = jsonify(
            {"message": "request made", "content": content_base64.decode("utf-8")}
        )
        return response


api.add_resource(GetImage, "/getimage")
api.add_resource(HelloWorld, "/")

if __name__ == "__main__":
    app.run()
