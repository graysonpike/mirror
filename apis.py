import requests
import json


WEATHER_URL_FORMAT = "https://query.yahooapis.com/v1/public/yql?q=select%%20*%%20from%%20weather.forecast%%20where%%20woeid%%20%%3D%%20%s&format=json&env=store%%3A%%2F%%2Fdatatables.org%%2Falltableswithkeys"



def get_weather(woeid):
	request = requests.get(WEATHER_URL_FORMAT % woeid)
	if request.status_code != 200: return None
	data = request.json()
	return data['query']['results']['channel']
