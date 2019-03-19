from flask import Flask, request, jsonify
from conf import dbconf
from conf.dbconf import dbsession
from entity.Models import User, Note
from sqlalchemy.sql import and_, or_, not_
from controller import NoteController


app = Flask(__name__, url_prefix="/api")


@app.route('/', methods=['GET'])
def index():
    return "Hello world???"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)