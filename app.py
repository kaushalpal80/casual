from flask import Flask, request
import json




app=Flask(__name__)


@app.route("/")
def home():
    return "Hello world"


@app.route('/cal',methods=["GET"])
def math_op():


    operation=request.json["operation"]
    number1= request.json["number1"]
    number2= request.json["number2"]

    if operation=="add":
        result=int(number1)+int(number2)

    # elif operation=="multiply":
    #     result= int(number1)*int(number2)
    
    # elif operation=="division":
    #     result = int(number1)/int(number2)

    else:
        print("The operation is not define")

    return str(result)

    

print(__name__)

if __name__=="__main__":
    app.run()