import sys
sys.path.append('/app/conf')
sys.path.append('/app/entity')
from flask import Blueprint, request, jsonify
from Models import User, Note
from sqlalchemy.sql import and_, or_, not_
from dbconf import ENGINE
from dbconf import dbsession

app = Blueprint("note", __name__, url_prefix="/api")

@app.route('/<username>/<notetitle>', methods=['GET'])
def getNote(username, notetitle):

    user = dbsession.query(User).filter(User.name==username).one_or_none()
    if user is None:
        return jsonify("no user")

    print(user)

    note = dbsession.query(Note).filter(and_(Note.userid == user.id, Note.title == notetitle)).one_or_none()
    if note is None:
        return jsonify("no note")

    return jsonify(
        user.name,
        note.title,
        note.text
    )

@app.route('/<username>/<notetitle>', methods=['POST'])
def saveNote(username, notetitle):

    text = request.json.get("text")
    if text is None:
        return jsonify("enter text"), 400

    if username is None or notetitle is None:
        return jsonify("invalid url")

    user = dbsession.query(User).filter(User.name==username).one_or_none()
    if user is None:
        return jsonify("no user"), 400

    note = dbsession.query(Note).filter(and_(Note.userid == user.id, Note.title == notetitle)).one_or_none()
    if note is None:
        note = Note()
        note.userid = user.id
        note.title = notetitle
        note.text = text
        dbsession.add(note)
    else:
        note.text = text

    dbsession.commit()
    return jsonify("saved!!")
