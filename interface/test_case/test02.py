import requests

url = "http://pc-api.power.com/index.php?c=Login&a=sendCode"
s = requests.session()
data = {
    "mobile": "139440937",
}
r = s.post(url, data=data)
print(r.json())
