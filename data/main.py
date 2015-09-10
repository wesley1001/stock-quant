#!/usr/bin/env python
# encoding: utf-8

import redis
import json
import tushare as ts
import pandas as pd

class DataHolder ():

    def __init__(self, stocks=[]):
        self.stocks = stocks
        if len(self.stocks) == 0:
            df = ts.get_stock_basics()
            df.to_json()

    def get_now_trans(self):
        for stock in self.stocks:
            pass


if __name__ == "__main__":
    d = DataHolder()
    print d.get_now_trans()

