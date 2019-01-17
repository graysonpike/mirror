import requests
import json
from requests_oauthlib import OAuth1


WEATHER_URL_FORMAT = "https://weather-ydn-yql.media.yahoo.com/forecastrss?&format=json&woeid=%s"


def get_weather(woeid, client_key, client_secret):
	auth = OAuth1(client_key, client_secret=client_secret)
	request = requests.get(WEATHER_URL_FORMAT % woeid, auth=auth)
	if request.status_code != 200:
		print("Recieved non-200 status code from Yahoo weather API call:")
		print(request.text)
		return None
	data = request.json()
	return data
