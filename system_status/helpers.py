r'''
                               |~~~~~~~|
                               |       |
                               |       |
                               |       |
                               |       |
                               |       |
    |~.\\\_\~~~~~~~~~~~~~~xx~~~         ~~~~~~~~~~~~~~~~~~~~~/_//;~|
    |  \  o \_         ,XXXXX),                         _..-~ o /  |
    |    ~~\  ~-.     XXXXX`)))),                 _.--~~   .-~~~   |
     ~~~~~~~`\   ~\~~~XXX' _/ ';))     |~~~~~~..-~     _.-~ ~~~~~~~
              `\   ~~--`_\~\, ;;;\)__.---.~~~      _.-~
                ~-.       `:;;/;; \          _..-~~
                   ~-._      `''        /-~-~
                       `\              /  /
                         |         ,   | |
                          |  '        /  |
                           \/;          |
                            ;;          |
                            `;   .       |
                            |~~~-----.....|
                           | \             \
                          | /\~~--...__    |
                          (|  `\       __-\|
                          ||    \_   /~    |
                          |)     \~-'      |
                           |      | \      '
                           |      |  \    :
                            \     |  |    |
                             |    )  (    )
                              \  /;  /\  |
                              |    |/   |
                              |    |   |
                               \  .'  ||
                               |  |  | |
                               (  | |  |
                               |   \ \ |
                               || o `.)|
                               |`\\) |
                               |       |
                               |       |

Author       : laysath faithleysath@gmail.com
Date         : 2023-07-20 18:57:08
LastEditors  : laysath faithleysath@gmail.com
LastEditTime : 2023-07-21 09:57:57
FilePath     : \qq-bot\src\plugins\system_status\helpers.py
Description  : 
GitHub       : https://github.com/faithleysath
'''


from datetime import datetime, timedelta

import humanize


def relative_time(time: datetime) -> timedelta:
    return datetime.now().astimezone() - time.astimezone()


def humanize_date(time: datetime) -> str:
    return humanize.naturaldate(time.astimezone())


def humanize_delta(delta: timedelta) -> str:
    return humanize.precisedelta(delta, minimum_unit="minutes")
