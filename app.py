from flask import Flask, request
import redis

app = Flask(__name__)
# regions = {"uk":"London","nigeria":"Lagos","southafrica":"Johannesburg", "usa":"DC", "us":"DC","ghana":"accra", "togo":"lome"}
version = "1.7.2"

r = redis.Redis(host="cache-server", port=6379)


@app.route("/getregion", methods = ["GET"])
def getregion():
    value = '<h1> Not found</h1>'
    country = request.args.get("country")


@app.route("/version")
def getversion():
    return version