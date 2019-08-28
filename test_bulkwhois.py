from flask import Flask
from flask_ipinfo import IPInfo
from ip2geotools.databases.noncommercial import DbIpCity

app = Flask(__name__)
ipinfo = IPInfo()

@app.route("/")
def hello():
    response = DbIpCity.get( ipinfo.ipaddress, api_key='free')
    return "Your IP Address is :" + response.ip_address

if __name__ == "__main__":
    app.run()