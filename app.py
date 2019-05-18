from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return 'Hello, world!'


@app.route('/info')
def info():
	return render_template('info.html')