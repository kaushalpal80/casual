from flask import *  
import json
app = Flask(__name__)  
  
@app.route('/login',methods = ['GET'])  
def login():  
      uname=request.json['uname']  
      passwrd=request.json['pass']  
      if uname=="ayush" and passwrd=="google":  
          return "Welcome %s" %uname  
   

if __name__ == '__main__':  
   app.run(debug = True)  