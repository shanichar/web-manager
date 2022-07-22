from webbrowser import get
import requests
def get_request():
    print("sending request...")
    r = requests.get("https://api.countapi.xyz/get/xactweather.herokuapp.com/8876e07a-824d-4b06-a0ee-090d0488e46a")
    print("archieved data in json format.")
    return r.json()
data = get_request()
val = data["value"]
print("your website has been visited "+str(val)+" times.")