import json, urllib
url = "https://query.yahooapis.com/v1/public/yql?q=select%20item.condition%20from%20weather.forecast%20where%20woeid%20%3D%20904987&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"

response = urllib.urlopen(url)

jdata = json.loads(response.read())

temp_in_f = int(jdata['query']['results']['channel']['item']['condition']['temp'])
temp_in_c = round((temp_in_f - 32)*5.0/9.0)

print(temp_in_c)
