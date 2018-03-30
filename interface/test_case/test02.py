import requests

url = "http://pc-api.power.com/index.php?c=Login&a=getAddressBook"
s = requests.session()
data = {
    "mobile": "139440937",
}
r = s.post(url)
print(r.json())
