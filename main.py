#!/usr/bin/env python
# encoding: utf-8

import data
import analytics

from quantdigger.kernel.engine.execute_unit import ExecuteUnit
from quantdigger.kernel.indicators.common import MA, BOLL
from quantdigger.kernel.engine.strategy import TradingStrategy
from quantdigger.util import  pcontract
import plotting

class DemoStrategy(TradingStrategy):
    """ 策略实例 """
    def __init__(self, exe):
        super(DemoStrategy, self).__init__(exe)
        # 创建平均线指标和布林带指标。其中MA和BOLL表示指标函数类。
        # 它们返回序列变量。
        # 'ma20'：指标名. 'b'画线颜色. ‘1‘: 线宽。如果无需
        # 绘图，则这些参数不需要给出。
        self.ma20 = MA(self, self.close, 20,'ma20', 'b', '1')
        self.ma10 = MA(self, self.close, 10,'ma10', 'y', '1')
        self.b_upper, self.b_middler, self.b_lower = BOLL(self, self.close, 10,'boll10', 'y', '1')

    def on_bar(self):
        """ 策略函数，对每根Bar运行一次。"""
        if self.ma10[1] < self.ma20[1] and self.ma10 > self.ma20:
            self.buy('long', self.open, 1, contract = 'IF000.SHFE')
        elif self.position() > 0 and self.ma10[1] > self.ma20[1] and self.ma10 < self.ma20:
            self.sell('long', self.open, 1)

        # 输出pcon1的当前K线开盘价格。
        print(self.open)

        # 夸品种数据引用
        # pcon2的前一根K线开盘价格。
        print(self.open_(1)[1])

if __name__ == '__main__':
    try:
        # 策略的运行对象周期合约
        pcon1 = pcontract('IF000.SHFE', '10.Minute')
        pcon2 = pcontract('IF000.SHFE', '10.Minute')
        # 创建模拟器，这里假设策略要用到两个不同的数据，比如套利。
        simulator = ExecuteUnit([pcon1, pcon2]);
        # 创建策略。
        algo = DemoStrategy(simulator)
        # 运行模拟器，这里会开始事件循环。
        simulator.run()

        # 显示回测结果
        plotting.plot_result(simulator.data[pcon], algo._indicators,
                            algo.blotter.deal_positions, algo.blotter)

    except Exception, e:
        print(e)
