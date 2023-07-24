from ..utils.scheduler_config import SchedulerConfig
from .platform import StatusChange
from httpx import AsyncClient
from ..types import Target, Category
from ..post import Post
from nonebot import logger

class ipShedConfig(SchedulerConfig):
    name = "dynamic_ip"
    schedule_type = "interval"
    schedule_setting = {"minutes": 2}

class ipStatus(StatusChange):
    categories = {1: "ipv6"}
    platform_name = "dynamic_ip"
    name = "动态IP地址状态"
    enable_tag = False
    enabled = True
    is_common = False
    scheduler = ipShedConfig
    has_target = False

    @classmethod
    async def get_target_name(cls, client: AsyncClient, target: Target) -> str | None:
        return "ipv6监控"
    
    async def get_status(self, _):
        res: str = (await self.client.get("https://v6r.ipip.net")).text
        logger.info(f"获取ip地址：{res}")
        return res
    
    def compare_status(self, _, old_status, new_status):
        s = f"{old_status} => {new_status}"
        res = []
        if old_status != new_status:
            logger.success("ip地址变更" + s)
            res.append(Post("dynamic_ip", text=s, target_name="ip地址变更"))
        else:
            logger.info("比较ip地址：" + s)

    def get_category(self, _):
        return Category(1)

    async def parse(self, raw_post):
        return raw_post