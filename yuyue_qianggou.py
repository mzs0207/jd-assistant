#!/usr/bin/env python
# -*- coding:utf-8 -*-
import datetime
import time

from jd_assistant import Assistant

if __name__ == '__main__':
    """
    重要提示：此处为示例代码之一，请移步下面的链接查看使用教程👇
    https://github.com/tychxn/jd-assistant/wiki/1.-%E4%BA%AC%E4%B8%9C%E6%8A%A2%E8%B4%AD%E5%8A%A9%E6%89%8B%E7%94%A8%E6%B3%95
    """


    def buy():

        sku_ids = '100011521400'  # 商品id
        area = '19_1607_3155'  # 区域id
        today = datetime.datetime.now()
        tomorow = today + datetime.timedelta(days=1)
        yue_yue_time = '{0} 21:00:00.5'.format(today.strftime("%Y-%m-%d"))  # 预约时间
        buy_time = '{0} 10:00:00.5'.format(tomorow.strftime("%Y-%m-%d"))
        asst = Assistant()  # 初始化
        asst.login_by_QRcode()  # 扫码登陆
        asst.make_reserve_by_time(sku_ids, yue_yue_time)  # 执行预约
        asst.exec_seckill_by_time(sku_ids, buy_time, 10, 0.5, 1)  # 执行抢购


    buy()

    # 6个参数：
    # sku_ids: 商品id。可以设置多个商品，也可以带数量，如：'1234' 或 '1234,5678' 或 '1234:2' 或 '1234:2,5678:3'
    # area: 地区id
    # wait_all: 是否等所有商品都有货才一起下单，可选参数，默认False
    # stock_interval: 查询库存时间间隔，可选参数，默认3秒
    # submit_retry: 提交订单失败后重试次数，可选参数，默认3次
    # submit_interval: 提交订单失败后重试时间间隔，可选参数，默认5秒
