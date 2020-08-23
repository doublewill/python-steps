import numpy as np
import requests
import json
response = requests.get("https://api.bilibili.com/x/web-interface/ranking");
data = response.text
result = json.loads(data)["data"]
note = result["note"]
list = np.array(result["list"])

print(note)
print(list)


