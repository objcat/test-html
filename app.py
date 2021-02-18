from flask import Flask, redirect
from flask import request
import json
from flask_cors import cross_origin
from flask_cors import CORS
import requests


app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/')
def hello_world():
    return redirect('/static/index.html')


@app.route("/api/v1/ttjjHistoryList")
@cross_origin(origins="*")
def ttjjHistoryList():
    code = request.args.get("code")
    pageSize = request.args.get("pageSize")

    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "product": "EFund",
        "FCODE": code,
        "pageSize": pageSize,
        "deviceid": "1",
        "version": "6.3.5",
        "MobileKey": "1",
        "pageIndex": "1",
        "appType": "ttjj",
        "plat": "Android"
    }

    res = requests.post("https://fundmobapi.eastmoney.com/FundMNewApi/FundMNHisNetList", headers=header, data=data)

    return {"result": json.loads(res.text)}


if __name__ == '__main__':
    app.run()
