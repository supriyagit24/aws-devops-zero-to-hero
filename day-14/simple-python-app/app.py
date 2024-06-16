from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Sagar, Please go to bed early!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')       
 
 
