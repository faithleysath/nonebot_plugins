from pydantic import BaseModel, Extra
from typing import List


class Config(BaseModel, extra=Extra.ignore):
    """Plugin Config Here"""
    is_block_group_enabled: bool = True
    """Whether to enable this plugin."""
    is_group_blacklist_mode: bool = False
    """Whether to use blacklist mode."""
    groups: list[str] = []
    """Group ID list."""