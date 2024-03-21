from flask import Flask, render_template,request
app = Flask(__name__)

from pymongo import MongoClient

conectin_string = "mongodb+srv://kvnvg2:GEepZ7Mf7zqVWP5G@cluster0.dniynqz.mongodb.net/"
Database = "FS_db"
col_Brukere = "Brukere"

def db_con_Brukere():
    connect = MongoClient(conectin_string)
    db = connect[Database]
    col = db[col_Brukere]
    return col

col = db_con_Brukere()
Brukere = col.find()


@app.route("/")
def Start():
    return render_template("index.html")



@app.route("/login_page")
def login_page():
    return render_template("login_page.html")



@app.route("/login", methods = ["POST"])
def login():
    if request.method == "POST":
        name = request.form["username"]
        password = request.form["pw"]
        for bruker in bruker in Brukere:
            if name == bruker["username"] and password == bruker["password"]:
                return render_template("start.html")
            else: return render_template("index.html")






if __name__ == "__main__":
    app.run(debug=True)