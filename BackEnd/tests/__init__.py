from flask import Flask

app = Flask(__name__)
from BackEnd.app import routes
from BackEnd.app import connection