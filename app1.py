"""from flask import Flask
app=Flask(__name__)
@app.route('/')
def home():
    return "Ranga is fucking Muttu"
app.run(debug=True)"""

"""from flask import Flask
app=Flask(__name__)
@app.route('/')
def home():
    return "<h1>Ranga is loving a girl name called nithya</h1>"
app.run(debug=True)"""

from flask import Flask, request, jsonify
app=Flask(__name__)
@app.route('/user')
def user():
    name= request.args.get('name')
    return f"<h1>Hello {name} </h1>"
@app.route('/add',methods=['POST'])
def add ():
    data=request.get_json()
    if not data:
        return jsonify({"error": "No data recieved"}), 400
    return jsonify(data)
app.run(debug=True)