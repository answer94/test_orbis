import flask
from flask import Flask
import db
flask.Response(response=None)
app = Flask(__name__)
object_db = db.Database()


@app.route('/object/', methods=['GET'])
@app.route('/object/<id>', methods=['GET'])
def get_obj(id=None):
    if id == None or id == str(0):
        obj = object_db.read_all()
    else:
        obj = object_db.read(id)

    return str(obj)



@app.errorhandler(500)
def internal_error(error):
    return "500 error"


@app.errorhandler(400)
def internal_error(error):
    return "400 error, введеное значение не цифра"


if __name__ == '__main__':
    app.run()
