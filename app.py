from flask import Flask, render_template, jsonify

app=Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'


@app.route('/greeting')
def greeting():
    return render_template('index.html', name="Akilah")


@app.route('/pie')
def pie():
    ingredients = ["Flour", "Butter", "Apples"]
    return jsonify({'pie ingredient': ingredients[0]})