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
Date         : 2023-07-20 20:03:08
LastEditors  : laysath faithleysath@gmail.com
LastEditTime : 2023-07-21 10:09:33
FilePath     : \qq-bot\src\plugins\block_groups\__init__.py
Description  : 
GitHub       : https://github.com/faithleysath
'''

from nonebot import get_driver, logger
from nonebot.plugin import PluginMetadata
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from nonebot.message import event_preprocessor
from nonebot.exception import IgnoredException
from .config import Config

__plugin_meta__ = PluginMetadata(
    name="群聊黑白名单",
    description="限定机器人生效群聊",
    usage="根据配置文件限定机器人作用域",
    config=Config,
    homepage="https://github.com/faithleysath/nonebot_plugins",
    extra={}
)

global_config = get_driver().config
cfg = Config.parse_obj(global_config)

@event_preprocessor
def block_processor(event: GroupMessageEvent):
    if cfg.is_group_blacklist_mode:
        if event.group_id in cfg.groups:
            if not cfg.is_block_group_enabled:
                logger.warning(f"群聊{event.group_id}在黑名单中，但是插件未启用")
                return
            logger.success(f"群聊{event.group_id}在黑名单中，忽略本条消息")
            raise IgnoredException("命中群聊黑名单")
    else:
        if event.group_id not in cfg.groups:
            if not cfg.is_block_group_enabled:
                logger.warning(f"群聊{event.group_id}不在白名单中，但是插件未启用")
                return
            logger.success(f"群聊{event.group_id}不在白名单中，忽略本条消息")
            raise IgnoredException("未命中群聊白名单")