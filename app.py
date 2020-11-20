from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/<parameter1>/<parameter2>')
def sum(parameter1,parameter2):
    add = int(parameter1) + int(parameter2)
    return jsonify(sum=add)

if __name__ == "__main__":
    app.run(debug=True)