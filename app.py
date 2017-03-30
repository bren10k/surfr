#!/usr/bin/env python

from __future__ import print_function
from datetime import datetime
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
    if beach == "jaws":
        coor = "10818"
        return coor, beach
    if beach == "kaisers":
        coor = "5536"
        return coor, beach
    if beach == "haleiwa":
        coor = "10834"
        return coor, beach
    if beach == "sandy":
        coor = "10837"
        return coor, beach
    if beach == "sunset":
        coor = "4746"
        return coor, beach
 
    if beach == "makaha":
        coor = "10845"
        return coor, beach
#    if beach == "glass":
#        coor = "21.901388,-159.587222&tp=24"
#        return coor, beach
 #   if beach == "hamoa":
 #       coor = "20.723055,-155.989722&tp=24"
 #       return coor, beach
#    if beach == "kaanapali":
#        coor = "20.941944,-156.695833&tp24"
#        return coor, beach
#    if beach == "kahana":
#        coor = "20.976666,-156.6825&tp24"
#        return coor, beach
    if beach == "waimea":
        coor = "4755"
        return coor, beach
    if beach == "turtle bay":
        coor = "59599"
        return coor, beach
    if beach == "makapuu":
        coor = "5540"
        return coor, beach
    if beach == "laniakea":
        coor = "4759"
        return coor, beach
    if beach == "waikiki":
        coor = "55536"
        return coor, beach
    if beach == "ala moana":
        coor = "5538"
        return coor, beach
    if beach == "yokohama":
        coor = "10844"
        return coor, beach
    if beach == "Hookipa":
        coor = "10817"
        return coor, beach
#    if beach == "Pakus":
#        coor = "20.910280,-156.485560&tp24"
#        return coor, beach
    if beach == "Honolua":
        coor = "10814"
        return coor, beach
  #  if beach == "Charley Young":
  #      coor = "20.729722,-156.453055&tp24"
  #      return coor, beach
 #   if beach == "Bakers beach":
 #       coor = "19.731111,-155.060833&tp24"
 #       return coor, beach
#    if beach == "Fleming":
#        coor = "21.003055,-156.669444&tp24"
 #       return coor, beach
    if beach == "Kahului Harbor":
        coor = "10816"
        return coor, beach
#    if beach == "Kalama Beach":
#        coor = "21.411944,-157.743888&tp24"
#        return coor, beach
#    if beach == "Kapiolani":
#        coor = "21.27,-157.825277&tp24"
 #       return coor, beach
#    if beach == "Kipu Kai":
#        coor = "21.913055,-159.392777&tp24"
#        return coor, beach
#    if beach == "Lanikai":
#        coor = "21.392222,-157.712&tp24"
#        return coor, beach
    if beach == "Hanalei":
        coor = "22.21444,-159.497777&tp24"
        return coor, beach
#    if beach == "Poipu":
#        coor = "21.878888,-159.4625&tp24"
#        return coor, beach
#    if beach == "1000 peaks":
#        coor = "20.793256,-156.57285&tp24"
#        return coor, beach
#    if beach == "Sugar Beach":
     #   coor = "20.785005,-156.466944&tp24"
    #    return coor, beach
   # if beach == "Wailea Beach":
  #      coor = "20.681288,-156.441944&tp24"
 #       return coor, beach
    if beach == "Rockpiles":
        coor = "4753"
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
    
    
    
  #  baseurl = "https://query.yahooapis.com/v1/public/yql?"
 #   yql_query = makeYqlQuery(data)
  #  if yql_query is None:
  #      return {}
#    yql_url = baseurl + urllib.parse.urlencode({'q': yql_query}) + "&format=json"
 #   result1 = urllib.request.urlopen(yql_url).read()
  #  data1 = json.loads(result1)
   # 
 #   qury = data1.get('query')
 #   
 #   result2 = qury.get('results')
 #   
 #   channel = result2.get('channel')
    
 #   item = channel.get('item')
  #  coor= item.get('lat') + ","  + item.get('long') + "&tp=24"
    
  #  return coor

#def makeYqlQuery(req):
#   result = req.get("result")
#    parameters = result.get("parameters")
#    city = parameters.get("geo-city")
#    if city is None:
 #       return None

  #  return "select * from weather.forecast where woeid in (select woeid from geo.places(1) where text='" + city + "')"


def makeWebhookResult(data, beach):
    
    time=str(datetime.now())
    tens = time[11] 
    print(tens)
   
    singles = time[12]
    print(singles)
    hour=int(tens + singles)
    period=0
    if hour <= 8:
        period=0
    if hour <= 14:
        period=1
    if hour <= 20:
        period == 2
    if hour < 24:
        period = 3
        
 
    
    surf=data.get('Surf')
    swellHeight=surf.get('swell_height1')
    zero=swellHeight[0]
    wind=data.get('Wind')
    windSpeed=wind.get('wind_speed')
    
   # astronomy=weather.get('astronomy')

    




   #  print(json.dumps(item, indent=4))

    speech = "Currently at "+ beach +" it is " + str(zero[period]) +" feet"

    
   

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
