r'''

　　┏┓　　　┏┓+ +
　┏┛┻━━━┛┻┓ + +
　┃　　　　　　　┃ 　
　┃　　　━　　　┃ ++ + + +
 ████━████ ┃+
　┃　　　　　　　┃ +
　┃　　　┻　　　┃
　┃　　　　　　　┃ + +
　┗━┓　　　┏━┛
　　　┃　　　┃　　　　　　　　　　　
　　　┃　　　┃ + + + +
　　　┃　　　┃
　　　┃　　　┃ +  神兽保佑
　　　┃　　　┃    代码无bug　　
　　　┃　　　┃　　+　　　　　　　　　
　　　┃　 　　┗━━━┓ + +
　　　┃ 　　　　　　　┣┓
　　　┃ 　　　　　　　┏┛
　　　┗┓┓┏━┳┓┏┛ + + + +
　　　　┃┫┫　┃┫┫
　　　　┗┻┛　┗┻┛+ + + +


Author       : laysath faithleysath@gmail.com
Date         : 2023-07-20 18:57:08
LastEditors  : laysath faithleysath@gmail.com
LastEditTime : 2023-07-23 17:37:49
FilePath     : \qq-bot\src\plugins\system_status\common.py
Description  : 
GitHub       : https://github.com/faithleysath
'''

from nonebot import on_command, on_type
from nonebot.adapters.onebot.v11 import PokeNotifyEvent
from . import server_status_command, status_config, status_permission, server_status_poke

if status_config.server_status_enabled:
    command = on_command(
        "status",
        aliases={"状态"},
        permission=status_permission,
        priority=10,
        handlers=[server_status_command],
    )
    """`status`/`状态` command matcher"""
    poke = on_type(PokeNotifyEvent, permission=status_permission, priority=10, handlers=[server_status_poke])
