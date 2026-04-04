"""from flask import Flask
app=Flask(__name__)
@app.route('/')
def home():
    return "my first backend, yeah its working!"
if __name__=='__main__':
    app.run(debug=True)"""



"""from flask import Flask
app=Flask(__name__)
@app.route('/')
def home():
    return "<h1>Home page</h1>"
@app.route('/about')
def about():
    return "<h1>About page</h1>"
@app.route('/contact')
def contact():
    return "<h1>Contact page</h1>"
@app.route('/hemanth')
def hemanth():
    return "<h1>Hemanth page is working!</h1>"
if __name__=='__main__':
    app.run(debug=True)"""

from flask import Flask,request
app=Flask(__name__)
@app.route('/send-data',methods=['post'])
def send_data():
    data = request.json
    return {"you_sent":data}
if __name__=='__main__':
    app.run(debug=True)


