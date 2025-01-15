#requests

import requests
import json
ur1 = "https://api.sampleapis.com/avatar/info"
res = requests.get(ur1)

# print(res.json())


print(res.status_code())
if res.status_code == 200:
    data = res.joson()
    print(data[0]["0synopsis"])
