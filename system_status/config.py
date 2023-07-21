r'''
                       ::
                      :;J7, :,                        ::;7:
                      ,ivYi, ,                       ;LLLFS:
                      :iv7Yi                       :7ri;j5PL
                     ,:ivYLvr                    ,ivrrirrY2X,
                     :;r@Wwz.7r:                :ivu@kexianli.
                    :iL7::,:::iiirii:ii;::::,,irvF7rvvLujL7ur
                   ri::,:,::i:iiiiiii:i:irrv177JX7rYXqZEkvv17
                ;i:, , ::::iirrririi:i:::iiir2XXvii;L8OGJr71i
              :,, ,,:   ,::ir@mingyi.irii:i:::j1jri7ZBOS7ivv,
                 ,::,    ::rv77iiiriii:iii:i::,rvLq@huhao.Li
             ,,      ,, ,:ir7ir::,:::i;ir:::i:i::rSGGYri712:
           :::  ,v7r:: ::rrv77:, ,, ,:i7rrii:::::, ir7ri7Lri
          ,     2OBBOi,iiir;r::        ,irriiii::,, ,iv7Luur:
        ,,     i78MBBi,:,:::,:,  :7FSL: ,iriii:::i::,,:rLqXv::
        :      iuMMP: :,:::,:ii;2GY7OBB0viiii:i:iii:i:::iJqL;::
       ,     ::::i   ,,,,, ::LuBBu BBBBBErii:i:i:i:i:i:i:r77ii
      ,       :       , ,,:::rruBZ1MBBqi, :,,,:::,::::::iiriri:
     ,               ,,,,::::i:  @arqiao.       ,:,, ,:::ii;i7:
    :,       rjujLYLi   ,,:::::,:::::::::,,   ,:i,:,,,,,::i:iii
    ::      BBBBBBBBB0,    ,,::: , ,:::::: ,      ,,,, ,,:::::::
    i,  ,  ,8BMMBBBBBBi     ,,:,,     ,,, , ,   , , , :,::ii::i::
    :      iZMOMOMBBM2::::::::::,,,,     ,,,,,,:,,,::::i:irr:i:::,
    i   ,,:;u0MBMOG1L:::i::::::  ,,,::,   ,,, ::::::i:i:iirii:i:i:
    :    ,iuUuuXUkFu7i:iii:i:::, :,:,: ::::::::i:i:::::iirr7iiri::
    :     :rk@Yizero.i:::::, ,:ii:::::::i:::::i::,::::iirrriiiri::,
     :      5BMBBBBBBSr:,::rv2kuii:::iii::,:i:,, , ,,:,:i@petermu.,
          , :r50EZ8MBBBBGOBBBZP7::::i::,:::::,: :,:,::i;rrririiii::
              :jujYY7LS0ujJL7r::,::i::,::::::::::::::iirirrrrrrr:ii:
           ,:  :@kevensun.:,:,,,::::i:i:::::,,::::::iir;ii;7v77;ii;i,
           ,,,     ,,:,::::::i:iiiii:i::::,, ::::iiiir@xingjief.r;7:i,
        , , ,,,:,,::::::::iiiiiiiiii:,:,:::::::::iiir;ri7vL77rrirri::
         :,, , ::::::::i:::i:::i:i::,,,,,:,::i:i:::iir;@Secbone.ii:::

Author       : laysath faithleysath@gmail.com
Date         : 2023-07-20 18:57:08
LastEditors  : laysath faithleysath@gmail.com
LastEditTime : 2023-07-21 09:57:09
FilePath     : \qq-bot\src\plugins\system_status\config.py
Description  : 
GitHub       : https://github.com/faithleysath
'''


from pydantic import Extra, BaseModel

CUR_CPU_TEMPLATE = r"当前CPU占用: {{ '%d' % cpu_usage['cur'] }}%"
"""Current CPU status template."""

MEDIAN15_CPU_TEMPLATE = r"15分钟中位CPU占用: {{ '%d' % cpu_usage['median15'] }}%"
"""15 minutes median CPU status template."""

AVG15_CPU_TEMPLATE = r"15分钟平均CPU占用: {{ '%d' % cpu_usage['avg15'] }}%"
"""15 minutes average CPU status template."""

MAX15_CPU_TEMPLATE = r"15分钟最大CPU占用: {{ '%d' % cpu_usage['max15'] }}%"
"""15 minutes maximum CPU status template."""

MIN15_CPU_TEMPLATE = r"15分钟最小CPU占用: {{ '%d' % cpu_usage['min15'] }}%"
"""15 minutes minimum CPU status template."""

# PER_CPU_TEMPLATE = (
#     "CPU:\n"
#     "{%- for core in per_cpu_usage %}\n"
#     "  core{{ loop.index }}: {{ '%02d' % core }}%\n"
#     "{%- endfor %}"

# )


MEMORY_TEMPLATE = r"内存: {{ '%d' % memory_usage.percent }}%"
"""Default memory status template."""

SWAP_TEMPLATE = (
    r"{% if swap_usage.total %}Swap: {{ '%d' % swap_usage.percent }}%{% endif %}"
)
"""Default swap status template."""

DISK_TEMPLATE = (
    "磁盘:\n"
    "{% for name, usage in disk_usage.items() %}\n"
    "  {{ name }}: {{ '%d' % usage.percent }}%\n"
    "{% endfor %}"
)
"""Default disk status template."""

UPTIME_TEMPLATE = "上线时间: {{ uptime | relative_time | humanize_delta }}"
"""Default uptime status template."""

RUNTIME_TEMPLATE = "运行时间: {{ runtime | relative_time | humanize_delta }}"
"""Default runtime status template."""

IPV6_TEMPLATE = "IPv6 地址: {{ ipv6_addr }}"


class Config(BaseModel, extra=Extra.ignore):
    server_status_enabled: bool = True
    """Whether to enable the server status commands."""
    server_status_truncate: bool = True
    """Whether to render the status template with used variables only."""
    server_status_only_superusers: bool = True
    """Whether to allow only superusers to use the status commands."""

    server_status_template: str = "\n".join(
        (CUR_CPU_TEMPLATE, MEDIAN15_CPU_TEMPLATE, AVG15_CPU_TEMPLATE, MAX15_CPU_TEMPLATE, MIN15_CPU_TEMPLATE, MEMORY_TEMPLATE, RUNTIME_TEMPLATE, DISK_TEMPLATE, IPV6_TEMPLATE)
    )
    """Default server status template.

    Including:

    - CPU usage
    - Memory usage
    - Runtime
    - Disk usage
    - IPV6 address
    """
