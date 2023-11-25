from flask import Flask,render_template
app = Flask(__name__)
print(__name__)

#but we can take username and password manually by suing variable rules in flask
@app.route('/')
def myhome():
    return render_template("index.html")


@app.route('/templates/project.html')
def blog():
    return render_template("project.html")


@app.route('/templates/privacy.html')
def blog3():
    return render_template("privacy.html")



@app.route('/templates/terms.html')
def blog2():
    return render_template("terms.html")


