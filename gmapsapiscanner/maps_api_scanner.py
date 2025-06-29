import requests
import warnings 
import json
import sys
import os
	

def scan_gmaps(apikey):
	vulnerable_apis = []
	
	url = "https://maps.googleapis.com/maps/api/staticmap?center=45%2C10&zoom=7&size=400x400&key="+apikey 
	response = requests.get(url, verify=False)
	if response.status_code == 200:
		print("API key is \033[1;31;40mvulnerable\033[0m for Staticmap API! Here is the PoC link:")
		print(url)
		vulnerable_apis.append("Staticmap || $2 per 1000 requests")
	elif b"PNG" in response.content:
		print("API key is not vulnerable for Staticmap API.")
		print("Reason: Manually check the "+url+" to view the reason.")
	else:
		print("API key is not vulnerable for Staticmap API.")
		print("Reason: "+ str(response.content))

	url = "https://maps.googleapis.com/maps/api/streetview?size=400x400&location=40.720032,-73.988354&fov=90&heading=235&pitch=10&key="+apikey 
	response = requests.get(url, verify=False)
	if response.status_code == 200:
		print("API key is \033[1;31;40mvulnerable\033[0m for Streetview API! Here is the PoC link:")
		print(url)
		vulnerable_apis.append("Streetview || $7 per 1000 requests")
	elif b"PNG" in response.content:
		print("API key is not vulnerable for Staticmap API.")
		print("Reason: Manually check the "+url+" to view the reason.")
	else:
		print("API key is not vulnerable for Staticmap API.")
		print("Reason: "+ str(response.content))

	url = "https://maps.googleapis.com/maps/api/directions/json?origin=Disneyland&destination=Universal+Studios+Hollywood4&key="+apikey
	response = requests.get(url, verify=False)
	if "error_message" not in response.text:
		print("API key is \033[1;31;40mvulnerable\033[0m for Directions API!")
		print(url)
		vulnerable_apis.append("Directions || $5 per 1000 requests")
		vulnerable_apis.append("Directions (Advanced) || $10 per 1000 requests")
	else:
		print("API key is not vulnerable for Directions API.")
		print("Reason: "+ response.json()["error_message"])

	url = "https://maps.googleapis.com/maps/api/geocode/json?latlng=40,30&key="+apikey 
	response = requests.get(url, verify=False)
	if "error_message" not in response.text:
		print("API key is \033[1;31;40mvulnerable\033[0m for Geocode API!")
		print(url)
		vulnerable_apis.append("Geocode || $5 per 1000 requests")
	else:
		print("API key is not vulnerable for Geocode API.")
		print("Reason: "+ response.json()["error_message"])

	url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=40.6655101,-73.89188969999998&destinations=40.6905615,-73.9976592&key="+apikey 
	response = requests.get(url, verify=False)
	if "error_message" not in response.text:
		print("API key is \033[1;31;40mvulnerable\033[0m for Distance Matrix API!")
		print(url)
		vulnerable_apis.append("Distance Matrix || $5 per 1000 elements")
		vulnerable_apis.append("Distance Matrix (Advanced) || $10 per 1000 elements")
	else:
		print("API key is not vulnerable for Distance Matrix API.")
		print("Reason: "+ response.json()["error_message"])

	url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=Museum%20of%20Contemporary%20Art%20Australia&inputtype=textquery&fields=photos,formatted_address,name,rating,opening_hours,geometry&key="+apikey
	response = requests.get(url, verify=False) 
	if "error_message" not in response.text:
		print("API key is \033[1;31;40mvulnerable\033[0m for Find Place From Text API!")
		print(url)
		vulnerable_apis.append("Find Place From Text || $17 per 1000 elements")
	else:
		print("API key is not vulnerable for Find Place From Text API.")
		print("Reason: "+ response.json()["error_message"])

	url = "https://maps.googleapis.com/maps/api/place/autocomplete/json?input=Bingh&types=(cities)&key="+apikey 
	response = requests.get(url, verify=False)
	if "error_message" not in response.text:
		print("API key is \033[1;31;40mvulnerable\033[0m for Autocomplete API!")
		print(url)
		vulnerable_apis.append("Autocomplete || $2.83 per 1000 requests")
		vulnerable_apis.append("Autocomplete Per Session || $17 per 1000 requests")
	else:
		print("API key is not vulnerable for Autocomplete API.")
		print("Reason: "+ response.json()["error_message"])

	url = "https://maps.googleapis.com/maps/api/elevation/json?locations=39.7391536,-104.9847034&key="+apikey 
	response = requests.get(url, verify=False)
	if "error_message" not in response.text:
		print("API key is \033[1;31;40mvulnerable\033[0m for Elevation API!")
		print(url)
		vulnerable_apis.append("Elevation || $5 per 1000 requests")
	else:
		print("API key is not vulnerable for Elevation API.")
		print("Reason: "+ response.json()["error_message"])

	url = "https://maps.googleapis.com/maps/api/timezone/json?location=39.6034810,-119.6822510&timestamp=1331161200&key="+apikey 
	response = requests.get(url, verify=False)
	if "errorMessage" not in response.text:
		print("API key is \033[1;31;40mvulnerable\033[0m for Timezone API!")
		print(url)
		vulnerable_apis.append("Timezone || $5 per 1000 requests")
	else:
		print("API key is not vulnerable for Timezone API.")
		print("Reason: "+ response.json()["errorMessage"])

	url = "https://roads.googleapis.com/v1/nearestRoads?points=60.170880,24.942795|60.170879,24.942796|60.170877,24.942796&key="+apikey 
	response = requests.get(url, verify=False)
	if "error" not in response.text:
		print("API key is \033[1;31;40mvulnerable\033[0m for Nearest Roads API!")
		print(url)
		vulnerable_apis.append("Nearest Roads || $10 per 1000 requests")
	else:
		print("API key is not vulnerable for Nearest Roads API.")
		print("Reason: "+ response.json()["error"]["message"])

	url = "https://www.googleapis.com/geolocation/v1/geolocate?key="+apikey 
	postdata = {'considerIp': 'true'}
	response = requests.post(url, data=postdata, verify=False)
	if "error" not in response.text:
		print("API key is \033[1;31;40mvulnerable\033[0m for Geolocation API!")
		print("curl -i -s -k -X POST -H 'Content-Type: application/json' -H 'Authorization: key="+apikey+"' https://fcm.googleapis.com/fcm/send -d '{\"registration_ids\":[\"ABC\"]}'")
		vulnerable_apis.append("Geolocation || $5 per 1000 requests")
	else:
		print("API key is not vulnerable for Geolocation API.")
		print("Reason: "+ response.json()["error"]["message"])

	url = "https://maps.googleapis.com/maps/api/place/details/json?place_id=ChIJN1t_tDeuEmsRUsoyG83frY4&fields=name,rating,formatted_phone_number&key="+apikey 
	response = requests.get(url, verify=False)
	if "error_message" not in response.text:
		print("API key is \033[1;31;40mvulnerable\033[0m for Place Details API!")
		print(url)
		vulnerable_apis.append("Place Details || $17 per 1000 requests")
	else:
		print("API key is not vulnerable for Place Details API.")
		print("Reason: "+ response.json()["error_message"])

	url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=100&types=food&name=harbour&key="+apikey 
	response = requests.get(url, verify=False)
	if "error_message" not in response.text:
		print("API key is \033[1;31;40mvulnerable\033[0m for Nearby Search-Places API!")
		print(url)
		vulnerable_apis.append("Nearby Search-Places || $32 per 1000 requests")
	else:
		print("API key is not vulnerable for Nearby Search-Places API.")
		print("Reason: "+ response.json()["error_message"])

	url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=restaurants+in+Sydney&key="+apikey 
	response = requests.get(url, verify=False)
	if "error_message" not in response.text:
		print("API key is \033[1;31;40mvulnerable\033[0m for Text Search-Places API!")
		print(url)
		vulnerable_apis.append("Text Search-Places || $32 per 1000 requests")
	else:
		print("API key is not vulnerable for Text Search-Places API.")
		print("Reason: "+ response.json()["error_message"])

	url = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=YOUR_PHOTO_REF&key="+apikey 
	response = requests.get(url, verify=False, allow_redirects=False)
	if response.status_code == 302:
		print("API key is \033[1;31;40mvulnerable\033[0m for Places Photo API!")
		print(url)
		vulnerable_apis.append("Places Photo || $7 per 1000 requests")
	else:
		print("API key is not vulnerable for Places Photo API.")
		print("Reason: Could not verify redirect")

	url = "https://fcm.googleapis.com/fcm/send" 
	postdata = '{"registration_ids":["ABC"]}'
	response = requests.post(url, data=postdata, verify=False, headers={'Content-Type':'application/json','Authorization':'key='+apikey})
	if response.status_code == 200:
		print("API key is \033[1;31;40mvulnerable\033[0m for FCM API!")
		print("curl --header \"Authorization: key="+apikey+"\" --header Content-Type:\"application/json\" https://fcm.googleapis.com/fcm/send -d '{\"registration_ids\":[\"ABC\"]}'")
		vulnerable_apis.append("FCM Takeover || https://abss.me/posts/fcm-takeover/")
	else:
		print("API key is not vulnerable for FCM API.")

	print("-------------------------------------------------------------")
	print("  Results || Cost Table/Reference to Exploit:")
	print("-------------------------------------------------------------")
	for api in vulnerable_apis:
		print("- " + api)
	print("-------------------------------------------------------------")
	print("Pricing reference:")
	print("https://cloud.google.com/maps-platform/pricing")
	print("https://developers.google.com/maps/billing/gmp-billing")

	# Skip JS prompt if running from Flask
	if os.getenv("NO_JSAPI") != "1":
		jsapi = input("Do you want to conduct tests for Javascript API? (Y/N) ")
		if jsapi.lower() == "y":
			with open("jsapi_test.html", "w") as f:
				f.write('<!DOCTYPE html><html><head><script src="https://maps.googleapis.com/maps/api/js?key='+apikey+'&callback=initMap&libraries=&v=weekly" defer></script><style>#map{height:100%;}html,body{height:100%;margin:0;padding:0;}</style><script>function initMap(){new google.maps.Map(document.getElementById("map"),{center:{lat:-34.397,lng:150.644},zoom:8});}</script></head><body><div id="map"></div></body></html>')
			print("jsapi_test.html created. Open in browser to confirm.")
			input("Press Enter to delete the file...")
			os.remove("jsapi_test.html")

warnings.filterwarnings("ignore")

if __name__ == "__main__":
	if len(sys.argv) > 2 and sys.argv[1] in ["--api-key", "-a"]:
		os.environ["NO_JSAPI"] = "1"
		scan_gmaps(sys.argv[2])
	elif len(sys.argv) == 1:
		apikey = input("Please enter the Google Maps API key you wanted to test: ")
		scan_gmaps(apikey)
	else:
		print("Usage:")
		print("  python maps_api_scanner.py --api-key <KEY>")