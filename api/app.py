from flask import Flask
from flask_cors import CORS

from routes.appRoutes import app_routes

app = Flask(__name__)
app.debug = True
CORS(app)
app_routes(app)

@app.route("/")
def hello_world():
    return "Hello World I hate u!"
