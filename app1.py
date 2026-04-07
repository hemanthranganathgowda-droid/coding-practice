"""from flask import Flask,request,jsonify
app=Flask(__name__)
@app.route('/user')

    
@app.route('/login',methods=['post'])
def login():
    data=request.json
    if data['user_name']=='Hemanth' and data['passward']=='1234':
        return jsonify({'message':'login sucessfully'})
    else:
        return jsonify({'message':'invalid user name'})
app.run(debug=True)"""


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
    {'username':'ravi',}
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
