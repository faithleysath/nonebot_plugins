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
Date         : 2023-07-20 18:57:08
LastEditors  : laysath faithleysath@gmail.com
LastEditTime : 2023-07-24 11:12:32
FilePath     : \qq-bot\src\plugins\system_status\data_source.py
Description  : 
GitHub       : https://github.com/faithleysath
'''


import asyncio
from datetime import datetime
from typing import TYPE_CHECKING, Dict, List, Optional

from .cpu_monitor import cpu_usages

import psutil
from nonebot import get_driver
from nonebot.log import logger
from nonebot.adapters import Bot
import httpx
import numpy as np

if TYPE_CHECKING:
    from psutil._common import sdiskusage

CURRENT_TIMEZONE = datetime.now().astimezone().tzinfo

driver = get_driver()

# bot status
_nonebot_run_time: datetime
_bot_connect_time: Dict[str, datetime] = {}


@driver.on_startup
async def _():
    global _nonebot_run_time
    _nonebot_run_time = datetime.now(CURRENT_TIMEZONE)


@driver.on_bot_connect
async def _(bot: Bot):
    _bot_connect_time[bot.self_id] = datetime.now(CURRENT_TIMEZONE)


@driver.on_bot_disconnect
async def _(bot: Bot):
    _bot_connect_time.pop(bot.self_id, None)


def get_nonebot_run_time() -> datetime:
    """Get the time when NoneBot started running."""
    try:
        return _nonebot_run_time
    except NameError:
        raise RuntimeError("NoneBot not running!") from None


def get_bot_connect_time() -> Dict[str, datetime]:
    """Get the time when the bot connected to the server."""
    return _bot_connect_time


def get_cpu_status() -> dict[str, float]:
    """Get the CPU usage status."""
    result = dict()
    result['cur'] = cpu_usages[-1]
    listed_cpu_usages = list(cpu_usages)[-900:]
    result['median15'] = np.median(listed_cpu_usages)
    result['avg15'] = np.mean(listed_cpu_usages)
    result['max15'] = max(listed_cpu_usages)
    result['min15'] = min(listed_cpu_usages)

    return result


async def per_cpu_status() -> List[float]:
    """Get the CPU usage status of each core."""
    psutil.cpu_percent(percpu=True)
    await asyncio.sleep(0.5)
    return psutil.cpu_percent(percpu=True)  # type: ignore


def get_memory_status():
    """Get the memory usage status."""
    return psutil.virtual_memory()


def get_swap_status():
    """Get the swap usage status."""
    return psutil.swap_memory()


def _get_disk_usage(path: str) -> Optional["sdiskusage"]:
    try:
        return psutil.disk_usage(path)
    except Exception as e:
        logger.warning(f"Could not get disk usage for {path}: {e!r}")


def get_disk_usage() -> Dict[str, "sdiskusage"]:
    """Get the disk usage status."""
    disk_parts = psutil.disk_partitions()
    return {
        d.mountpoint: usage
        for d in disk_parts
        if (usage := _get_disk_usage(d.mountpoint))
    }


def get_uptime() -> datetime:
    """Get the uptime of the mechine."""
    return datetime.fromtimestamp(psutil.boot_time(), tz=CURRENT_TIMEZONE)

async def get_ipv6() -> str:
    """Get the ipv6 address of the machine."""
    # Access https://v6r.ipip.net/ to get the ipv6 address
    url = 'https://v6r.ipip.net/'
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
            return response.text
        except:
            return "获取失败"
