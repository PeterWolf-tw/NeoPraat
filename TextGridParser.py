#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# FileName: TextGridParser.py

# Developer: Peter. w (peter.w@droidtown.co)


#Copyright (c) 2016 Droidtown Linguistic Tech. Co.
#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
#associated documentation files (the "Software"), to deal in the Software without restriction,
#including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
#and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
#subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all copies or substantial
#portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
#LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
#WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


import re


sizePat = re.compile(r"size = \d+")
xminPat = re.compile(r"xmin = \d+\.?\d*")
xmaxPat = re.compile(r"xmax = \d+\.?\d*")

class TextGridParser:
    def __init__(self, TextGridFile):
        self.TextGrid = open(TextGridFile, "r").read()
        itemLIST = self.TextGrid.split("    item ")
        self.TextGridTierSize = int(re.findall(sizePat, itemLIST[0])[0].split(" ")[-1])
        self.TextGridxmin = float(re.findall(xminPat, itemLIST[0])[0].split(" ")[-1])
        self.TextGridxmax = float(re.findall(xmaxPat, itemLIST[0])[0].split(" ")[-1])

        self.TextGridDICT = {}

        for i in itemLIST[1:]:
            i = i.replace(" ", "")
            tmpItemLIST = i.split("\n")
            self.TextGridDICT["item_{0}".format(tmpItemLIST[0].replace("[", "").replace("]:", ""))] = {}
            self.TextGridDICT["item_{0}".format(tmpItemLIST[0].replace("[", "").replace("]:", ""))]["class"] = tmpItemLIST[1].split("=")[1].replace('"', "")
            self.TextGridDICT["item_{0}".format(tmpItemLIST[0].replace("[", "").replace("]:", ""))]["name"] = tmpItemLIST[2].split("=")[1].replace('"', "")
            self.TextGridDICT["item_{0}".format(tmpItemLIST[0].replace("[", "").replace("]:", ""))]["xmin"] = float(tmpItemLIST[3].split("=")[1])
            self.TextGridDICT["item_{0}".format(tmpItemLIST[0].replace("[", "").replace("]:", ""))]["xmax"] = float(tmpItemLIST[4].split("=")[1])
            self.TextGridDICT["item_{0}".format(tmpItemLIST[0].replace("[", "").replace("]:", ""))]["size"] = int(tmpItemLIST[5].split("=")[1])
            self.TextGridDICT["item_{0}".format(tmpItemLIST[0].replace("[", "").replace("]:", ""))]["intervals"] = []
            for interval in range(0, len(tmpItemLIST[6:]), 4):
                if tmpItemLIST[6:][interval] == "":
                    pass
                else:
                    self.TextGridDICT["item_{0}".format(tmpItemLIST[0].replace("[", "").replace("]:", ""))]["intervals"].append([int(tmpItemLIST[6:][interval].split("[")[1].split("]")[-2]),
                                                                                                                                 float(tmpItemLIST[6:][interval+1].split("=")[1]),
                                                                                                                                 float(tmpItemLIST[6:][interval+2].split("=")[1]),
                                                                                                                                 tmpItemLIST[6:][interval+3].split("=")[1].replace('"', ""),
                                                                                                                                 ])
        return None




if __name__== "__main__":
    #interval structure = [interval_number, xmin, xmax, text]

    tg = TextGridParser("./sample.TextGrid")
    print(tg.TextGridDICT.keys())
    for k in tg.TextGridDICT.keys():
        print(tg.TextGridDICT[k].keys())

