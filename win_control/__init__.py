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
LastEditTime : 2023-07-21 16:47:57
FilePath     : \qq-bot\src\plugins\win_control\__init__.py
Description  : 
GitHub       : https://github.com/faithleysath
'''
from datetime import timedelta

from nonebot import get_driver
from nonebot.plugin import PluginMetadata
from nonebot import on_command
from nonebot.permission import SUPERUSER
from nonebot.adapters.onebot.v12 import PrivateMessageEvent, Message
from nonebot.params import CommandArg
from nonebot.log import logger

from .config import Config

from .control import (
    shutdown,
    reboot,
)

global_config = get_driver().config
config = Config.parse_obj(global_config)

__plugin_meta__ = PluginMetadata(
    name="服务器系统控制",
    description="控制服务器的关机、重启等操作",
    usage=(
        "通过发送指令 `控制/control` 获取可用命令列表\n"
        "可以通过配置文件修改服务器状态模板"
    ),
    type="application",
    homepage="https://github.com/faithleysath/nonebot_plugins",
    config=Config,
    supported_adapters=None,
)

command_list = {
    ("关机", "shutdown"): shutdown,
    ("重启", "reboot"): reboot,
}

ctrl = on_command(
    cmd="control", 
    aliases={"控制", "ctrl", "执行"}, 
    priority=11, 
    permission=SUPERUSER, 
    block=False, 
    )

@ctrl.handle()
async def handle_command(event: PrivateMessageEvent, args: Message = CommandArg()):
    arg = args.extract_plain_text()
    logger.warning(f"侦测到指令：{arg}")
    if arg == "":
        await ctrl.finish("请输入指令")
    else:
        for key in command_list.keys():
            if arg in key:
                command_list[key]()
                await ctrl.finish(f"{arg}指令执行成功")
        await ctrl.finish(f"{arg}指令不存在")