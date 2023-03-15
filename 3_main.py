from flask import Flask, request

app = Flask(__name__)


@app.route('/sum3/', methods=['POST'])
def sum_array():
    content = request.json
    array = content.values()
    return {"sum": sum(array)}


app.run(debug=True)
