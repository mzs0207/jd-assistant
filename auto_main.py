#!/usr/bin/env python
# coding:utf8
import json
import time
import threading
import datetime

from jd_assistant import Assistant

config = {}


def load_config():
    """

    :return:
    """
    global config
    with open('config.json') as f:
        config = json.load(f)


def save_config():
    """

    :return:
    """
    global config
    with open('config.json', 'w') as f:
        json.dump(config, f, sort_keys=True, indent=4, separators=(",", ":"))


def keep_cookie():
    """

    :return:
    """
    global config
    while True:
        try:
            load_config()
            for account in config["accounts"]:
                print("keep {0} activate.".format(account))
                js = Assistant(account)
                js.keep()
        except Exception as e:
            print(e)
        time.sleep(600)


if __name__ == '__main__':
    k = threading.Thread(target=keep_cookie)
    k.start()

    while True:
        try:
            load_config()
            now = datetime.datetime.now()
            n = 0
            for task in config["tasks"]:
                print(task)
                if  task['finish'] == 0:
                    t = datetime.datetime.strptime(task['task_start_time'], "%Y-%m-%d %H:%M:%S.%f")
                    if now > t:
                        if task['action_type'] == "yuyue":
                            jd = Assistant(task['account'])
                            jd.login_by_QRcode()  # 扫码登陆
                            th = threading.Thread(target=jd.make_reserve_by_time,
                                                  args=(task["sku_ids"], task["action_time"]))
                            th.start()
                            config["tasks"][n]['finish'] = 1
                        elif task['action_type'] == "buy":
                            jd = Assistant(task['account'])
                            jd.login_by_QRcode()  # 扫码登陆
                            th = threading.Thread(target=jd.exec_seckill_by_time,
                                                  args=(
                                                      task["sku_ids"], task["action_time"], task["retry"],
                                                      task["interval"],
                                                      task["num"]))
                            th.start()
                            config["tasks"][n]['finish'] = 1
                n += 1

            save_config()

        except Exception as e:
            print(e)
        time.sleep(10)

