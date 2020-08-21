import numpy as np
from numpy import *
import json
import re
import matplotlib.pyplot as plt

from numpy import *
def create_dataset():
    ss = "A010106"
    with open("query.json", "r", encoding="utf-8") as files:
     f = json.loads(files.read())
     datanodes = np.array(f["returndata"]["datanodes"])
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
    print(y)
    # plt.figure()
    # plt.plot(x, y)
    # plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    create_dataset()

