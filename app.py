from flask import Flask
import redis

app = Flask(__name__)
regions = {"uk":"London","nigeria":"Lagos","southafrica":"Johannesburg", "usa":"DC", "us":"DC","ghana":"accra", "togo":"lome"}
version = "1.6"

r = redis.Redis(host="cache-server", port=6379)



@app.route("/getregion/<country>")
def lookup(country):
    value ="N/A"
    try:
        value = r.get(country)
    except:
        pass
    return value 


@app.route("/getsaveregion/<country>/<city>")
def savedata(country, city):
    value ="pass"
    try:
        r.set(country, city)
    except:
        value = "fail"
    return value


@app.route("/version")
def getversion():
    return version