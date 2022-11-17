from flask import Flask
import db

app = Flask(__name__)
object_db = db.Database()


@app.route('/object/', methods=['GET'])
@app.route('/object/<id>', methods=['GET'])
def users(id=None):
    if id == None or id == str(0):
        users = object_db.read_all()
    else:
        users = object_db.read(id)

    return users


@app.errorhandler(500)
def internal_error(error):
    return "500 error"


@app.errorhandler(400)
def internal_error(error):
    return "400 error, введеное значение не цифра"


if __name__ == '__main__':
    app.run()
