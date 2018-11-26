from flask import *
from flask_sqlalchemy import *
# from pymysql import *
import operator
# import pymysql

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:m,590718@localhost/mml'
db = SQLAlchemy(app)


class exper(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    URL = db.Column(db.CHAR(10))
    code = db.Column(db.CHAR(20))
    textee = db.Column(db.TEXT)

    def __init__(self, url, code, text):
        self.URL = url
        self.code = code
        self.textee = text


@app.route('/')
def index():
    # name = None
    return render_template('main.html')


@app.route('/register', methods=['POST'])
def register():
    text = request.form.get("text")
    name = request.form.get("uid")
    net = exper('3', name, text)  # soon not complete the function' URL'
    db.session.add(net)
    db.session.commit()
    return redirect('/search/'+str(net.id))


@app.route('/search/<idx>', methods=["GET"])
def search(idx):
    fid = exper.query.get(idx)
    if fid is None:
        return "The record is blank or has been removed", 404
    else:
        return render_template('search.html', content=fid.textee, idp=idx)


@app.route('/search/<idx>/verify', methods=["POST"])
def verify(idx):
    fid = exper.query.get(idx)
    key = request.form.get('identify')
    if fid is None:
        return "The record isn't exist or has been removed", 404
    elif operator.eq(fid.code, key) is False:
        return "The identity you had input is valid", 404
    else:
        return render_template('modify.html',idp=idx, text=fid.textee)


@app.route('/search/<idx>/modify', methods=["POST"])
def modify(idx):
    fid = exper.query.get(idx)
    fid.textee = request.form.get("text")
    db.session.commit()
    return redirect('/search/' + str(idx))


if __name__ == '__main__':
    app.run()

