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


@app.route("/api/v1/ttjj/ttjjHistoryList")
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

@app.route("/api/v1/ttjj/kList")
@cross_origin(origins="*")
def kList():
    code = request.args.get("code")
    pageSize = request.args.get("pageSize")

    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "secid": "0." + code,
        "fields1": "f1,f2,f3,f4,f5,f6,f7,f8,f8,f10,f11",
        "fields2": "f51,f52,f53,f54,f55,f56,f57",
        "fqt": "0",
        "lmt": "80",
        "end": "20300101ut=128d100d314be19f356035cb850fe90c",
        "klt": "101",
        "authorityType": "fa"
    }

    res = requests.get("https://push2his.eastmoney.com/api/qt/stock/kline/get", headers=header, data=data)

    return {"result": json.loads(res.text)}


if __name__ == '__main__':
    app.run()
