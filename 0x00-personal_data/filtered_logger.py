#!/usr/bin/env python3
""" obfuscate logs """

import re
from typing import List


def filter_datum(fields: List, redaction: str, message: str, separator: str) -> str:
    """obfuscate log data"""
    for field in fields:
        message = re.sub(r"(?<=" + field + r"=)[^"
                         + separator + r"]+", redaction, message)
    return message
