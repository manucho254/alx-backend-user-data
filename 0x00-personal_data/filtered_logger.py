#!/usr/bin/env python3
""" obfuscate logs """

import re
from typing import List


def create_pattern(fields: List[str], sep: str) -> str:
    """create regex pattern for fields"""
    return "|".join(
        [re.escape(field) + r"=[^" + sep +
         "]+(?=" + sep + ")" for field in fields]
    )


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """obfuscate log data"""
    return re.sub(create_pattern(fields, separator),
                  lambda x: x.group(0).split("=")[0] + "="
                  + redaction, message)
