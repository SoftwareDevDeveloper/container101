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

    try:
        city = r.get (country)
        value = '''<h1> {} is in {} </h1>'''.format(city, country)
    except:
        pass

    return value


@app.route("/saveregion", methods = ["GET"])
def saveregion():
    country = request.args.get("country")
    city = request.args.get("city")

    value = "<h1> failed to save </h1>"

    try:
        r.set(country, city)
        value = '''<h1> {} is in {} saved successfully </h1>'''.format(city, country)
    except:
        pass
        
    return value


@app.route("/version")
def getversion():
    return version