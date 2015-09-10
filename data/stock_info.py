#!/usr/bin/env python
# encoding: utf-8

import tushare as ts

class Stock ():
    def __init__(self, stockCode, start, end):
        self._stockCode = stockCode
        self._start     = start
        self._end       = end

