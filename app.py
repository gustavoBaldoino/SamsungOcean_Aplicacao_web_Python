from flask import Flask, render_template

app = Flask("Hello")

@app.route("/")
def hello():
	return "-->> Hello Word"

@app.route("/meucontato")
def meuContato():
    return render_template('index.html')