r'''
                       _oo0oo_
                      o8888888o
                      88" . "88
                      (| -_- |)
                      0\  =  /0
                    ___/`---'\___
                  .' \\|     |// '.
                 / \\|||  :  |||// \
                / _||||| -:- |||||- \
               |   | \\\  - /// |   |
               | \_|  ''\---/''  |_/ |
               \  .-\__  '-'  ___/-. /
             ___'. .'  /--.--\  `. .'___
          ."" '<  `.___\_<|>_/___.' >' "".
         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
         \  \ `_.   \_ __\ /__ _/   .-` /  /
     =====`-.____`.___ \_____/___.-`___.-'=====
                       `=---='


     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

           佛祖保佑     永不宕机     永无BUG

Author       : laysath faithleysath@gmail.com
Date         : 2023-07-20 22:47:55
LastEditors  : laysath faithleysath@gmail.com
LastEditTime : 2023-07-21 09:57:22
FilePath     : \qq-bot\src\plugins\system_status\cpu_monitor.py
Description  : 
GitHub       : https://github.com/faithleysath
'''


import subprocess
import threading
from collections import deque
from typing import Deque

cpu_usages: Deque[float] = deque(maxlen=900)

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def cpu_monitor(cmd = r'typeperf "\Processor Information(_Total)\% Processor Utility"'
                      , output = cpu_usages):
    """CPU占用率监控线程，将输出结果添加到列表中，每1秒输出一次，保存3600秒"""
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    for line in iter(process.stdout.readline, b''):
        try:
            line = line.decode().strip().split(',')[-1].strip('"')  # 读取输出结果
        except UnicodeDecodeError:
            line = "null"
        if is_float(line):
            output.append(float(line))  # 将输出结果添加到列表中

def start_cpu_monitor():
    """启动CPU占用率监控线程"""
    thread = threading.Thread(target=cpu_monitor)
    thread.start()
