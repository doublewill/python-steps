import numpy as np
import json
import re
import matplotlib.pyplot as plt
import demjson
# 数据取自 https://data.stats.gov.cn/easyquery.htm?cn=C01
import chardet

from numpy import *

def query_json(jsonData):
    with open(jsonData, "r", encoding="utf-8") as files:
        f = json.dumps(files.read(), ensure_ascii=False)
        res = json.loads(f)
        return demjson.decode(res)

def create_dataset(ss):
        a = query_json("query.json")
        datanodes = np.array(a["returndata"]["datanodes"])
        wdnodes = np.array(a["returndata"]["wdnodes"])
        zbnodes = wdnodes[0]["nodes"]
        sjnodes = wdnodes[1]["nodes"]

        for item in zbnodes:
            # print(isinstance(item["cname"], unicode))
            cname = item["cname"].encode("utf-8")
                    # str.encode()
            # print(chardet.detect(cname))

            # tname = cname.decode("utf-8")

            # gname = tname.encode("gbk")
            # print(gname)
        # print(np.array(sjnodes["nodes"]))

        # print(json.dumps(test["exp"], ensure_ascii=False, indent=2))
        # print(np.array(a["returndata"]["wdnodes"]))
        filter_arr = []
        for item in datanodes:
            if re.search(ss, item["code"]):
                filter_arr.append(True)
            else:
                filter_arr.append(False)

        draw_figure(datanodes[filter_arr])


def draw_figure(list):
    x = []
    y = []

    for item in list:
        y.append(item["data"]["data"])
        x.append(item["code"].split(".")[2])

    x.reverse()
    y.reverse()
    plt.figure()
    plt.plot(x, y, ".r--", linewidth=2)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.title("gdp")
    plt.ylabel("gdp值 【亿元】")
    plt.xlabel("时间")
    plt.grid(True)
    plt.show()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    create_dataset("A020106")
