from flask import Flask, render_template, request
from Database import *
app = Flask(__name__)

@app.route("/")
def Home():
    return render_template("Registration.html")

@app.route("/Registration_links", methods = ["POST", "GET"])
def Registration():
    link = request.form.get("link")
    if request.method == "POST":
        if link == "Teacher":
            return render_template("ForTeacherRegistration.html")
        elif link == "Student":
            return render_template("ForStudentRegistration.html")
    else:
        return render_template("Registration.html")

@app.route("/Inputs", methods = ["GET", "POST"])
def StudentRegistration():
    if request.method == "POST":
        firstname = str(request.form["firstname"])
        middlename = str(request.form["middlename"])
        lastname = str(request.form["lastname"])
        age = int(request.form["age"])
        address = str(request.form["address"])
        sex = str(request.form["sex"])
        cellphone_number = str(request.form["cellphone_number"])
        Birth_date = str(request.form["Birth_date"])
        Birth_place = str(request.form["Birth_place"])

        ForStudentRegistration(
            firstname, middlename, lastname, age, address, sex, 
            cellphone_number, Birth_date, Birth_place
        )
        
        x = "Registered Successfully!"
        return render_template("ForStudentRegistration.html", x = x)
    
    else:
        x = "Registration failed!"
        return render_template("ForStudentRegistration.html")

if __name__ == "__main__":
    app.run(debug = True)