#!/usr/bin/env python3
""" obfuscate logs """

import re
from typing import List


def replace_value(field: str, message: str, repl: str, sep: str) -> str:
    """replace a value"""
    return re.sub(r"(?<=" + field + r"=)[^" + sep + r"]+", repl, message)


def filter_datum(fields: List[str], redaction: str, message: str, separator) -> str:
    """obfuscate log data"""
    for field in fields:
        message = replace_value(field, message, redaction, separator)
    return message
