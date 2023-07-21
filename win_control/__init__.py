r'''
                                                    __----~~~~~~~~~~~------___
                                   .  .   ~~//====......          __--~ ~~
                   -.            \_|//     |||\\  ~~~~~~::::... /~
                ___-==_       _-~o~  \/    |||  \\            _/~~-
        __---~~~.==~||\=_    -_--~/_-~|-   |\\   \\        _/~
    _-~~     .=~    |  \\-_    '-~7  /-   /  ||    \      /
  .~       .~       |   \\ -_    /  /-   /   ||      \   /
 /  ____  /         |     \\ ~-_/  /|- _/   .||       \ /
 |~~    ~~|--~~~~--_ \     ~==-/   | \~--===~~        .\
          '         ~-|      /|    |-~\~~       __--~~
                      |-~~-_/ |    |   ~\_   _-~            /\
                           /  \     \__   \/~                \__
                       _--~ _/ | .-~~____--~-/                  ~~==.
                      ((->/~   '.|||' -_|    ~~-/ ,              . _||
                                 -_     ~\      ~~---l__i__i__i--~~_/
                                 _-~-__   ~)  \--______________--~~
                               //.-~~~-~_--~- |-------~~~~~~~~
                                      //.-~~~--\
                      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                              神兽保佑            永无BUG

Author       : laysath faithleysath@gmail.com
Date         : 2023-07-21 09:54:05
LastEditors  : laysath faithleysath@gmail.com
LastEditTime : 2023-07-21 10:08:29
FilePath     : \qq-bot\src\plugins\win_control\__init__.py
Description  : 
GitHub       : https://github.com/faithleysath
'''

from nonebot import get_driver
from nonebot.plugin import PluginMetadata

from .config import Config

global_config = get_driver().config
config = Config.parse_obj(global_config)

__plugin_meta__ = PluginMetadata(
    name="服务器系统控制",
    description="控制服务器的开机、关机、重启等操作",
    usage=(
        "通过发送指令 `控制/control` 获取可用命令列表\n"
        "可以通过配置文件修改服务器状态模板"
    ),
    type="application",
    homepage="https://github.com/faithleysath/nonebot_plugins",
    config=Config,
    supported_adapters=None,
)