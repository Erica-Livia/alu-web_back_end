#!/usr/bin/env python3
import re


"""
define a function called filter_datum
"""


def filter_datum(fields, redaction, message, separator):
    pattern = '|'.join(f'(?<={field}=)[^{separator}]+' for field in fields)
    return re.sub(pattern, redaction, message)
