from flask import Flask, render_template, request, url_for 
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# app.config["SQLALCHEMY_DATABASE_URI"]='sqlite://db.sqlite'
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
# db = SQLAlchemy(app)

# class Todo(db.Model):
#    id = db.Column(db.Integer , primary_key=True)
#    title = db.COlumn(db.String(100))
#    complete = db.Column(db.Boolean)

# db.create_all()

@app.route("/", methods=["GET","POST"])
def home():
    app.logger.debug("main debug")
    if request.method == "POST":
        if "This" in request.form:
            return render_template("this.html")     
        elif "That" in request.form:
            return render_template("that.html")

    return render_template("homepage.html")

    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

