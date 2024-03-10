import re
from functools import reduce


_leading_ws = re.compile('^(\s+)\w')

def wilt(fp, *, indent=4) -> int:
    """
    Calculate WILT metric.

    It stands for Whitespace Integrated over Lines of Text, and it's
    measured in indentations.
    """

    return reduce(lambda r, l: r + sum(len(ws) for ws in _leading_ws.findall(l)), fp, 0) / indent
