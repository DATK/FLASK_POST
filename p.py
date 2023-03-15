from flask import Flask,request
import requests

app = Flask(__name__)


@app.route('/sum2/', methods=['POST'])
def sum_array():
    print(request.json)
    data = request.json['data']
    suma=sum(data)
    dc={"sum": suma}
    return dc
    
    

app.run(debug=True)
