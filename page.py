from flask import Flask, render_template,request

app = Flask(__name__)

@app.rout("/register",methods=["GET","POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        gender = request.form["gender"]
        age = request.form["age"]
        qual = request.form["qual"]
        stream = request.form["stream"]
        address = request.form["address"]
        return render_template("register.html",name=name,gender=gender,age=age,qual=qual,stream=stream,address=address)
    else:
        return render_template("register.html")