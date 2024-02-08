#!/usr/bin/env python3
""" obfuscate logs """

import re
from typing import List
import logging


def create_pattern(fields: List[str], sep: str) -> str:
    """create regex pattern for fields"""
    return "|".join(
        [re.escape(field) + r"=[^" + sep + "]+(?=" + sep
         + ")" for field in fields]
    )


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """obfuscate log data"""
    return re.sub(
        create_pattern(fields, separator),
        lambda x: x.group(0).split("=")[0] + "=" + redaction,
        message,
    )


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Initialize classs """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self._fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Format the LogRecord into a string """
        formatted = logging.Formatter(self.FORMAT).format(record)
        return filter_datum(self._fields, self.REDACTION,
                            formatted, self.SEPARATOR)
