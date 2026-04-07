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


from flask import Flask,request
app=Flask(__name__)
@app.route('/login')
def login():
    username=request.args.get('username')
    passward=request.args.get('passward')
    if username=='hemanth' and passward=='1234':
        return "login successfully"
    else:
        return "invalid user name"
app.run(debug=True)