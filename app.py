#!/usr/bin/env python

from __future__ import print_function
from future import standard_library
standard_library.install_aliases()
import urllib.request, urllib.parse, urllib.error
import json
import os


from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def processRequest(req):
    baseurl = "http://api.worldweatheronline.com/premium/v1/marine.ashx?key=41c9cef29f974bd48c2192134173101&format=json&q="
 
    
    query = getCoor(req)
    surl = baseurl + query
    result = urllib.request.urlopen(surl).read()

    data = json.loads(result)

    res = makeWebhookResult(data)
    return res


def getCoor(data):
    
    result = data.get("result")
    parameters = result.get("parameters")
    city = parameters.get("geo-city")
    beach = parameters.get("beach")
    
    if beach == "north shore":
        coor = "20.934431,-156.355957&tp=24"
        return coor
    if beach == "south shore":
        coor ="20.626836,-156.443873&tp=24"
        return coor
    if beach == "west shore":
        coor ="20.864596,-156.673628&tp=24"
        return coor
    if beach == "east shore":
        coor = "20.759070,-155.985446&tp=24"
        return coor
    if beach == "pipeline":
        coor = "21.662271,-158.052622&tp=24"
        return coor
    if beach == "Maalaea":
        coor = "20.779166,-156.490555&tp=24"
        return coor
    if beach == "Big Beach":
        coor = "20.632863,-156.448751&tp=24"
        return coor
    if beach == "jaws":
        coor = "20.93861,-156.26083&tp=24"
        return coor
    if beach == "kaisers":
        coor = "21.280057,-157.840791&tp=24"
        return coor
    if beach == "haleiwa":
        coor = "21.594145,-158.108148&tp=24"
        return coor
    if beach == "sandy":
        coor = "21.287255,-157.669247&tp=24"
        return coor
    if beach == "sunset":
        coor = "21.676104,-158.040433&tp=24"
        return coor
    if beach == "kewalo":
        coor = "21.290113,-157.859301&tp=24"
        return coor
    if beach == "bellows":
        coor = "21.362532,-157.709341&tp=24"
        return coor
    if beach == "makaha":
        coor = "21.469045,-158.223048&tp=24"
        return coor
    if beach == "glass":
        coor = "21.901388,-159.587222&tp=24"
        return coor
    if beach == "hamoa":
        coor = "20.723055,-155.989722&tp=24"
        return coor
    if beach == "kaanapali":
        coor = "20.941944,-156.695833&tp24"
        return coor
    if beach == "kahana":
        coor = "20.976666,-156.6825&tp24"
        return coor
    
    
    
    
    
    
    
    
    

    baseurl = "https://query.yahooapis.com/v1/public/yql?"
    yql_query = makeYqlQuery(data)
    if yql_query is None:
        return {}
    yql_url = baseurl + urllib.parse.urlencode({'q': yql_query}) + "&format=json"
    result1 = urllib.request.urlopen(yql_url).read()
    data1 = json.loads(result1)
    
    qury = data1.get('query')
    
    result2 = qury.get('results')
    
    channel = result2.get('channel')
    
    item = channel.get('item')
    coor= item.get('lat') + ","  + item.get('long') + "&tp=24"
    
    return coor

def makeYqlQuery(req):
    result = req.get("result")
    parameters = result.get("parameters")
    city = parameters.get("geo-city")
    if city is None:
        return None

    return "select * from weather.forecast where woeid in (select woeid from geo.places(1) where text='" + city + "')"


def makeWebhookResult(data):
    
    data1=data.get('data')
    weather=data1.get('weather')
    zero=weather[0]
    hourly=zero.get('hourly')
    hourly1=hourly[0]
   # astronomy=weather.get('astronomy')




   #  print(json.dumps(item, indent=4))

    speech = "Currently it is " + hourly1.get('swellHeight_ft') + " feet"

    
   

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        "data": {
            "google": {
                "expect_user_response": "false",
                 }
            }

          }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
