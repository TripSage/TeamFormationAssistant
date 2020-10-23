from flask import Flask

app = Flask(__name__)

from app import routes
from app import connection

if __name__ == "__main__":
    app.run(debug=True)