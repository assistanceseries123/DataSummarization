from flask import Flask,render_template
import requests
from flask import request as req
from flask import url_for

app=Flask(__name__)

@app.route('/',methods=["GET","POST"])
def index():

    return render_template("index.html")

@app.route("/Summarize",methods=["GET","POST"])
def summarize():

    if req.method=="POST":

        API_URL = "https://api-inference.huggingface.co/models/sshleifer/distilbart-cnn-12-6"
        headers = {"Authorization": "Bearer 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"}
        data=req.form["data"]
        maxL=int(req.form["maxL"])
        minL=maxL//4
        def query(payload):
             
             response=response.post(API_URL,headers=headers,json=payload)
             return response.json()
        output=query({
             "inputs":data,
             "parameters":{"min_length":minL,"max_length":maxL},
        })[0]
        return render_template("index.html",result=output['summary_text'])
    else:
         return render_template("index.html")
    
if __name__=="__main__":
      app.run(debug=True)