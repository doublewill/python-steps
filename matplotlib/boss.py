import  numpy as np
import requests
import json
import  demjson
response = requests.get("https://www.zhipin.com/wapi/zpCommon/data/position.json").text
positionJson = json.loads(response)
positionList = positionJson["zpData"]

subLevelModelList = positionList[1]["subLevelModelList"]
def getSubLevelModelListByCode(subLevelModelList, code):
    subList = []
    for child in subLevelModelList:
        if child["code"] == code:
            subList = child["subLevelModelList"]

    return subList

subLevelModel1 = getSubLevelModelListByCode(subLevelModelList, 100900)
# print(np.array(positionList))
# print(demjson.decode(positionJson, encoding="utf-8"))
# print(response["zpData"])
print(np.array(subLevelModel1))


