import numpy as np
import json
import re
import matplotlib.pyplot as plt
import demjson
# 数据取自 https://data.stats.gov.cn/easyquery.htm?cn=C01

from numpy import *

def create_dataset():
    ss = "A010106"
    with open("query.json", "r", encoding="utf-8") as files:
        f = json.dumps(files.read())
        res = json.loads(f)
        a = demjson.decode(res)

        datanodes = np.array(a["returndata"]["datanodes"])
        filter_arr = []
        for item in datanodes:
            if re.search(ss, item["code"]):
                filter_arr.append(True)
            else:
                filter_arr.append(False)

        draw_figure(datanodes[filter_arr])


def draw_figure(list):
    x = range(0, len(list))
    y = []
    for item in list:
        y.append(item["data"]["data"])
    plt.figure()
    plt.plot(x, y, ".r--", linewidth=2)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.title("gdp")
    plt.ylabel("gdp值 【亿元】")
    plt.xlabel("时间")
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    create_dataset()
