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
    
    if beach == "north shore":
        coor = "20.934431,-156.355957&tp=24"
        return coor, beach
    if beach == "south shore":
        coor ="20.626836,-156.443873&tp=24"
        return coor, beach
    if beach == "west shore":
        coor ="20.864596,-156.673628&tp=24"
        return coor, beach
    if beach == "east shore":
        coor = "20.759070,-155.985446&tp=24"
        return coor, beach
    if beach == "pipeline":
        coor = "21.665553,-158.052948&tp=24"
        return coor, beach
    if beach == "Maalaea":
        coor = "20.779166,-156.490555&tp=24"
        return coor, beach
    if beach == "Big Beach":
        coor = "20.632863,-156.448751&tp=24"
        return coor, beach
    if beach == "jaws":
        coor = "20.93861,-156.26083&tp=24"
        return coor, beach
    if beach == "kaisers":
        coor = "5536"
        return coor, beach
    if beach == "haleiwa":
        coor = "21.594145,-158.108148&tp=24"
        return coor, beach
    if beach == "sandy":
        coor = "21.287255,-157.669247&tp=24"
        return coor, beach
    if beach == "sunset":
        coor = "21.676104,-158.040433&tp=24"
        return coor, beach
    if beach == "kewalo":
        coor = "21.290113,-157.859301&tp=24"
        return coor, beach
    if beach == "bellows":
        coor = "21.362532,-157.709341&tp=24"
        return coor, beach
    if beach == "makaha":
        coor = "21.469045,-158.223048&tp=24"
        return coor, beach
    if beach == "glass":
        coor = "21.901388,-159.587222&tp=24"
        return coor, beach
    if beach == "hamoa":
        coor = "20.723055,-155.989722&tp=24"
        return coor, beach
    if beach == "kaanapali":
        coor = "20.941944,-156.695833&tp24"
        return coor, beach
    if beach == "kahana":
        coor = "20.976666,-156.6825&tp24"
        return coor, beach
    if beach == "waimea":
        coor = "21.643272,-158.069449&tp24"
        return coor, beach
    if beach == "turtle bay":
        coor = "21.701392,-157.999757&tp24"
        return coor, beach
    if beach == "makapuu":
        coor = "21.286325,-157.707475&tp24"
        return coor, beach
    if beach == "lanikai":
        coor = "21.393208,-157.715151&tp24"
        return coor, beach
    if beach == "waikiki":
        coor = "21.393208,-157.824686&tp24"
        return coor, beach
    if beach == "ala moana":
        coor = "21.289009,-157.849328&tp24"
        return coor, beach
    if beach == "yokohama":
        coor = "21.548557,-158.24319&tp24"
        return coor, beach
    if beach == "Hookipa":
        coor = "20.933214,-156.357524&tp24"
        return coor, beach
    if beach == "Pakus":
        coor = "20.910280,-156.485560&tp24"
        return coor, beach
    if beach == "Honolua":
        coor = "21.011896,-156.636854&tp24"
        return coor, beach
    if beach == "Charley Young":
        coor = "20.729722,-156.453055&tp24"
        return coor, beach
    if beach == "Bakers beach":
        coor = "19.731111,-155.060833&tp24"
        return coor, beach
    if beach == "Fleming":
        coor = "21.003055,-156.669444&tp24"
        return coor, beach
    if beach == "Kahului Harbor":
        coor = "20.894722,-156.476666&tp24"
        return coor, beach
    if beach == "Kalama Beach":
        coor = "21.411944,-157.743888&tp24"
        return coor, beach
    if beach == "Kapiolani":
        coor = "21.27,-157.825277&tp24"
        return coor, beach
    if beach == "Kipu Kai":
        coor = "21.913055,-159.392777&tp24"
        return coor, beach
    if beach == "Lanikai":
        coor = "21.392222,-157.712&tp24"
        return coor, beach
    if beach == "Hanalei":
        coor = "22.21444,-159.497777&tp24"
        return coor, beach
    if beach == "Poipu":
        coor = "21.878888,-159.4625&tp24"
        return coor, beach
    if beach == "1000 peaks":
        coor = "20.793256,-156.57285&tp24"
        return coor, beach
    if beach == "Waimea Bay":
        coor = "21.641505,-158.067127&tp24"
        return coor, beach
    if beach == "Sugar Beach":
        coor = "20.785005,-156.466944&tp24"
        return coor, beach
    if beach == "Wailea Beach":
        coor = "20.681288,-156.441944&tp24"
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
    
    analysis=data.get('Analysis')
    surfRange=analysis.get('surfRange')
    zero=surfRange[0]
   
   # astronomy=weather.get('astronomy')

    




   #  print(json.dumps(item, indent=4))

    speech = "Currently at "+ beach +" it is " + zero

    
   

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
