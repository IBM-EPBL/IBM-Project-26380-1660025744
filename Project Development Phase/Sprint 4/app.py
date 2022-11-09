import os
import numpy as np 
from flask import Flask,request,render_template 
import pickle


app= Flask(__name__)

@app.route("/") 
def about():
    return render_template("about.html")

@app.route("/about")
def home():
    return render_template("about.html")

@app.route("/info") 
def information():
    return render_template("info.html")

@app.route("/upload")
def test():
    return render_template("predict.html")

@app.route("/predict",methods=["GET","POST"]) 
def upload():
    if request.method=='POST':
        print(request)
        model = pickle.load(open('model.pkl','rb'))
        # pred=model.predict(x)
        return 1    
    return None

if __name__=="__main__":
    app.run(debug=False,port=5500)
            
            