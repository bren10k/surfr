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
 
    result = req.get("queryResult")
    
    query, beach = getCoor(result)
    surl = baseurl + query
    result = urllib.request.urlopen(surl).read()

    data = json.loads(result)

    res = makeWebhookResult(data, beach)
    return res


def getCoor(data):
    
    result = data.get("result")
    parameters = result.get("parameters")
   
    beach = parameters.get("beach")
    coor="0000"
    
    if beach == "pipeline":
        coor = "4750"
        
    if beach == "Maalaea":
        coor = "7443"
       
    if beach == "Big Beach":
        coor = "5520"
        
    if beach == "Jaws":
        coor = "10818"
       
    if beach == "Kaisers":
        coor = "5536"
     
    if beach == "Haleiwa":
        coor = "10834"
    
    if beach == "Sandy's":
        coor = "10837"
       
    if beach == "Sunset":
        coor = "4746"
        
    if beach == "Makaha":
        coor = "10845"
      
    if beach == "Kaanapali":
        coor = "10812"
        
    if beach == "Kahana":
        coor = "10812"
       
    if beach == "Waimea Bay":
        coor = "4755"
        
    if beach == "Turtle Bay":
        coor = "59599"
       
    if beach == "Makapuu":
        coor = "5540"
       
    if beach == "Laniakea":
        coor = "4759"
       
    if beach == "Waikiki":
        coor = "55536"
       
    if beach == "Ala Moana":
        coor = "5538"
       
    if beach == "Yokohama":
        coor = "10844"
       
    if beach == "Honolua":
        coor = "10814"
        
    if beach == "Hookipa":
        coor = "10817"    
       
    if beach == "Kahului Harbor":
        coor = "10816"
        
    if beach == "Hanalei":
        coor = "5522"
        
    if beach == "Poipu":
        coor = "5526"
        
    if beach == "Wailea Beach":
        coor = "5521"
        
    if beach == "Rockpiles":
        coor = "5537"
        
    if beach == "Velzyland":
        coor = "10833"
        
    if beach == "Log Cabins":
        coor = "4754"
        
    if beach == "Barbers Point":
        coor = "10847"
        
    if beach == "Ewa Beach":
        coor = "10848"
        
    if beach == "Diamond Head":
        coor = "4760"
        
    if beach == "Off the Wall":
        coor = "4752"
        
    if beach == "Kahuku":
        coor = "10841"
        
    if beach == "Olowalu":
        coor = "10809"
        
    if beach == "La Perouse":
        coor = "10811"
        
    if beach == "Kanaha":
        coor = "10813"
       
    if beach == "Honomanu":
        coor = "10819"
       
    if beach == "Tavares Bay":
        coor = "108155"
    
    if beach == "Hana Bay":
        coor = "10820"
       
    if beach == "The Cove":
        coor = "10810"
   
    if beach == "Mana Point":
        coor = "10831"
       
    if beach == "Polihale":
        coor = "10830"
        
    if beach == "Haena Bay":
        coor = "5523"
      
    if beach == "Pakala":
        coor = "5527"
       
    if beach == "PKs":
        coor = "125523"
        
    if beach == "Kailua":
        coor = "10838"
      
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

    WindDir = wdir(wind, windPeriod)




   #  print(json.dumps(item, indent=4))

    speech = "Currently at "+ beach +" it is " + str(surf_minz[period]) +" to " +str(surf_maxz[period])+ " feet. With " + WindDir + " Wind Speeds of " + str("{0:.2f}".format(todayWindSpeed[windPeriod])) + " Miles per hour"

    
   

    print("Response:")
    print(speech)

    return {
        "fulfillmentText": speech

          }

def wdir(wind, period):
    wind_direction = wind.get('wind_direction')
    wdirToday = wind_direction[0]
    wDegree = wdirToday[period]
    
    if wDegree >= 15 and wDegree < 45:
        direction = "North North East"
    if wDegree > 60 and wDegree < 75:
        direction = "East North East"
    if wDegree > 30 and wDegree < 60:
        direction = "North East"
    if wDegree > 75 and wDegree <= 105:
        direction = "East"
    if wDegree > 105 and wDegree <= 165:
        direction = "South East"
    if wDegree > 165 and wDegree <= 195:
        direction = "South"
    if wDegree > 195 and wDegree <= 255:
        direction = "South West"
    if wDegree > 255 and wDegree <= 285:
        direction = "West"
    if wDegree > 285 and wDegree <= 345:
        direction = "North West"
    if wDegree > 345 and wDegree < 15:
        direction = "North"
        
    return direction
    
    
    
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
