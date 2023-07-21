r'''
                       .::::.
                     .::::::::.
                    :::::::::::
                 ..:::::::::::'
              '::::::::::::'
                .::::::::::
           '::::::::::::::..
                ..::::::::::::.
              ``::::::::::::::::
               ::::``:::::::::'        .:::.
              ::::'   ':::::'       .::::::::.
            .::::'      ::::     .:::::::'::::.
           .:::'       :::::  .:::::::::' ':::::.
          .::'        :::::.:::::::::'      ':::::.
         .::'         ::::::::::::::'         ``::::.
     ...:::           ::::::::::::'              ``::.
    ````':.          ':::::::::'                  ::::..
                       '.:::::'                    ':'````..

Author       : laysath faithleysath@gmail.com
Date         : 2023-07-21 10:26:06
LastEditors  : laysath faithleysath@gmail.com
LastEditTime : 2023-07-21 16:50:51
FilePath     : \qq-bot\src\plugins\win_control\control.py
Description  : 实现系统控制功能
GitHub       : https://github.com/faithleysath
'''

import os
import platform
from nonebot.log import logger

def shutdown():
    logger.success("执行关机操作")
    if platform.system() == "Windows":
        os.system("shutdown /s /t 0")
    elif platform.system() == "Linux":
        os.system("sudo shutdown -h now")

def reboot():
    logger.success("执行重启操作")
    if platform.system() == "Windows":
        os.system("shutdown /r /t 0")
    elif platform.system() == "Linux":
        os.system("sudo shutdown -r now")