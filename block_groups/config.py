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
Date         : 2023-07-23 16:53:26
LastEditors  : laysath faithleysath@gmail.com
LastEditTime : 2023-07-23 17:20:00
FilePath     : \qq-bot\src\plugins\block_groups\config.py
Description  : 
GitHub       : https://github.com/faithleysath
'''

from pydantic import BaseModel, Extra
from typing import List


class Config(BaseModel, extra=Extra.ignore):
    """Plugin Config Here"""
    is_block_group_enabled: bool = False
    """Whether to enable this plugin."""
    is_group_blacklist_mode: bool = False
    """Whether to use blacklist mode."""
    groups: List[str] = []
    """Group ID list."""