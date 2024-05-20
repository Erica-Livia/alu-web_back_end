#!/usr/bin/env python3
"""
define a function called filter_datum
"""

import re
from typing import List


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str
        ) -> str:
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
