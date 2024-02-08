#!/usr/bin/env python3
""" obfuscate logs """

import re
from typing import List


def replace_value(field: str, message: str, repl: str, sep: str) -> str:
    """replace a value"""
    return re.sub(r"(?<=" + field + r"=)[^" + sep + r"]+", repl, message)


def filter_datum(fields: List[str], redaction: str, message: str, separator) -> str:
    """obfuscate log data"""
    return re.sub(
        r"{}(?={})".format(separator + "|".join(fields), separator), redaction, message
    )
