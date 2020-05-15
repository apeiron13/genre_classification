from flask_cors import CORS
from flask import Flask
from config import *

from Genre import Genre

app = Flask(__name__)

genre = Genre()

CORS(app, resources={r"/*": {"origins": "*"}})
