from flask import Flask
import redis

app = Flask(__name__)
# regions = {"uk":"London", "nigeria":"Lagos", "southafrica":"Johannesburg", "usa":"DC", "us":"DC","ghana":"accra", "togo":"lome"}
version = "1.7.1"

r = redis.Redis(host="cache-server", port=6379)


@app.route("/getregion/<country>")
def lookup(country):
    value = "N/A"
    try:
        value = r.get (country)
    except:
        pass
    return value


app.route("/saveregion/<country>/<city>")
def savedata(country, city):
    value = "N/A"
    try:
        value = r.set(country, city)
    except:
        pass
    return value


@app.route("/version")
def getversion():
    return version

























# from flask import Flask

# app = Flask(__name__)
# regions = {"uk":"London", "nigeria":"Lagos", "southafrica":"Johannesburg", "usa":"DC", "us":"DC","ghana":"accra", "togo":"lome"}
# version = "1.6"


# @app.route("/getregion/<country>")
# def lookup(country):
#     value = "N/A"
#     try:
#         value = regions [country.lower()]
#     except:
#         pass
#     return value


# @app.route("/version")
# def getversion():
#     return version