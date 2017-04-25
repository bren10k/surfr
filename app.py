#!/usr/bin/env python

from __future__ import print_function

from datetime import datetime
from future import standard_library
standard_library.install_aliases()
import urllib.request, urllib.parse, urllib.error
import json
import os
from pytz import timezone
import pytz

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
    baseurl = "http://api.surfline.com/v1/forecasts/"
 
    
    query, beach = getCoor(req)
    surl = baseurl + query
    result = urllib.request.urlopen(surl).read()

    data = json.loads(result)

    res = makeWebhookResult(data, beach)
    return res


def getCoor(data):
    
    result = data.get("result")
    parameters = result.get("parameters")
    city = parameters.get("geo-city")
    beach = parameters.get("beach")
    
    if beach == "pipeline":
        coor = "4750"
        return coor, beach
    if beach == "Maalaea":
        coor = "7443"
        return coor, beach
    if beach == "Big Beach":
        coor = "5520"
        return coor, beach
    if beach == "Jaws":
        coor = "10818"
        return coor, beach
    if beach == "Kaisers":
        coor = "5536"
        return coor, beach
    if beach == "Haleiwa":
        coor = "10834"
        return coor, beach
    if beach == "Sandy's":
        coor = "10837"
        return coor, beach
    if beach == "Sunset":
        coor = "4746"
        return coor, beach
    if beach == "Makaha":
        coor = "10845"
        return coor, beach
    if beach == "Kaanapali":
        coor = "10812"
        return coor, beach
    if beach == "Kahana":
        coor = "10812"
        return coor, beach
    if beach == "Waimea Bay":
        coor = "4755"
        return coor, beach
    if beach == "Turtle Bay":
        coor = "59599"
        return coor, beach
    if beach == "Makapuu":
        coor = "5540"
        return coor, beach
    if beach == "Laniakea":
        coor = "4759"
        return coor, beach
    if beach == "Waikiki":
        coor = "55536"
        return coor, beach
    if beach == "Ala Moana":
        coor = "5538"
        return coor, beach
    if beach == "Yokohama":
        coor = "10844"
        return coor, beach
    if beach == "Hookipa":
        coor = "10817"
        return coor, beach
    if beach == "Honolua":
        coor = "10814"
        return coor, beach
    if beach == "Kahului Harbor":
        coor = "10816"
        return coor, beach
    if beach == "Hanalei":
        coor = "5522"
        return coor, beach
    if beach == "Poipu":
        coor = "5526"
        return coor, beach
    if beach == "Wailea Beach":
        coor = "5521"
        return coor, beach
    if beach == "Rockpiles":
        coor = "5537"
        return coor, beach
    if beach == "Velzyland":
        coor = "10833"
        return coor, beach
    if beach == "Log Cabins":
        coor = "4754"
        return coor, beach
    if beach == "Barbers Point":
        coor = "10847"
        return coor, beach
    if beach == "Ewa Beach":
        coor = "10848"
        return coor, beach
    if beach == "Diamond Head":
        coor = "4760"
        return coor, beach
    if beach == "Off the Wall":
        coor = "4752"
        return coor, beach
    if beach == "Kahuku":
        coor = "10841"
        return coor, beach
    if beach == "Olowalu":
        coor = "10809"
        return coor, beach
    if beach == "La Perouse":
        coor = "10811"
        return coor, beach
    if beach == "Kanaha":
        coor = "10813"
        return coor, beach
    if beach == "Honomanu":
        coor = "10819"
        return coor, beach
    if beach == "Tavares Bay":
        coor = "108155"
        return coor, beach
    if beach == "Hana Bay":
        coor = "10820"
        return coor, beach
    if beach == "The Cove":
        coor = "10810"
        return coor, beach
    if beach == "Mana Point":
        coor = "10831"
        return coor, beach
    if beach == "Polihale":
        coor = "10830"
        return coor, beach
    if beach == "Haena Bay":
        coor = "5523"
        return coor, beach
    if beach == "Pakala":
        coor = "5527"
        return coor, beach
    if beach == "PKs":
        coor = "125523"
        return coor, beach
    if beach == "Kailua":
        coor = "10838"
        return coor, beach
    if beach == "Lahaina Harbor":
        coor = "5528"
        return coor, beach


def makeWebhookResult(data, beach):
    fmt = "%Y-%m-%d %H:%M:%S %Z%z"
    now_utc = datetime.now(timezone('UTC'))
    now_hawaii = now_utc.astimezone(timezone('US/Hawaii'))
 #   time=str(datetime.now(timezone('UTC'))
    time = now_hawaii.strftime(fmt)
    print(time)
    tens = time[11] 
    print(tens)
   
    singles = time[12]
    print(singles)
    hour=int(tens + singles)
    period=0
    windPeriod=0
    
    if hour < 24:
        period = 3
        windPeriod=7
    if hour < 23:
        windPeriod=6
    if hour < 20:
        period = 2
        windPeriod=5
    if hour < 17:
        windPeriod=4
    if hour < 14:
        windPeriod=3
        period = 1
    if hour < 11:
        windPeriod=2
    if hour < 8:
        windPeriod=1
        period = 0
    if hour < 5:
        windPeriod=0
    if hour <= 2:
        windPeriod=0
        
    
    surf=data.get('Surf')
    surf_min=surf.get('surf_min')
    surf_minz=surf_min[0]
    surf_max=surf.get('surf_max')
    surf_maxz=surf_max[0]
    swellHeight=surf.get('swell_height1')
    
    wind=data.get('Wind')
    windSpeed=wind.get('wind_speed')
    todayWindSpeed= windSpeed[0]
    
   # astronomy=weather.get('astronomy')

    




   #  print(json.dumps(item, indent=4))

    speech = "Currently at "+ beach +" it is " + str(surf_minz[period]) +" to " +str(surf_maxz[period])+ " feet. With Wind Speeds of " + str("{0:.2f}".format(todayWindSpeed[windPeriod])) + " Miles per hour"

    
   

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
