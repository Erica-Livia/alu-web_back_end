#!/usr/bin/env python3
import re
from typing import List

"""
define a function called filter_datum
"""


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    filter_datum functioni
    parameters:
        fieds: list
        redaction: string
        message: string
        separator
    """
    pattern = '|'.join(f'(?<={field}=)[^{separator}]+' for field in fields)
    return re.sub(pattern, redaction, message)
