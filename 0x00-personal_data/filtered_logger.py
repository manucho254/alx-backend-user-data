#!/usr/bin/env python3
""" obfuscate logs """

import re
from typing import List
import logging

PII_FIELDS = ("email", "phone", "ssn", "password", "last_login")


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
        record.msg = filter_datum(self._fields, self.REDACTION,
                                  record.msg, self.SEPARATOR)
        return super().format(record)


def get_logger() -> logging.Logger:
    """ get logger function """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)

    return logger
