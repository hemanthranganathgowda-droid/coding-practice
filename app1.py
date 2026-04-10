

"""from flask import Flask,request
app=Flask(__name__)
@app.route('/login')
def login():
    username=request.args.get('username')
    passward=request.args.get('passward')
    if username=='hemanth' and passward=='1234':
        return "login successfully"
    else:
        return "invalid user name"
app.run(debug=True)"""

from flask import Flask,request
app=Flask(__name__)
users=[
    {'username':'hemanth','password':'1234'},
    {'username':'ravi','password':'5678'}
]
@app.route('/login',methods=['POST'])
def logic():
    data=request.json
    username=data['username']
    password=data['password']
    for user in users:
        if user['username']==username and user['password']==password:
            return "login sucess"
        return "invalid user"
app.run(debug=True)
from flask import Flask,request,jsonify
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Create a table (Model)
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    branch = db.Column(db.String(50))

# Create database
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return "Database Connected Successfully 🚀"

if __name__ == '__main__':
    app.run(debug=True)