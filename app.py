from flask import Flask

app = Flask(__name__)
regions = {"uk":"London", "nigeria":"Lagos", "southafrica":"Johannesburg", "usa":"DC", "us":"DC","ghana":"accra", "togo":"lome"}
version = "1.6"


@app.route("/getregion/<country>")
def lookup(country):
    value = "N/A"
    try:
        value = regions [country.lower()]
    except:
        pass
    return value


@app.route("/version")
def getversion():
    return version