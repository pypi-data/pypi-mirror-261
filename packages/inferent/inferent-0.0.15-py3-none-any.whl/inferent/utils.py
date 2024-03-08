"""String and math utility functions."""

from functools import partial
from math import sqrt
from scipy import interpolate
import string


def ct(s: str) -> str:
    """ct = cleantext

    Takes a utf-8 string and converts to ascii lower case without punctuation
    """
    if not s:
        return ""
    return (
        s.encode("utf-8")
        .decode("ascii", "ignore")
        .translate(str.maketrans("", "", string.punctuation))
        .lower()
        .strip()
    )


def curve_fn(curve="spline", x=None, y=None):
    """
    TODO: increasing?

    steep_circular:
    ===============
    See https://www.desmos.com/calculator/hjactjjo2n

    x < x2: y = a - b \sqrt{ 1 - ((x - d)/c)^2 }

    with the constraints:
    - pass through x1, y1; x2, y2;
    - left side of curve (slope -infty) at x1
    - bottom of curve (slope 0) at x2

    we find that:
    > a = y1
    > b = y1 - y2
    > c = x2 - x1
    > d = x2

    x > x2: y = a + b \sqrt{ 1 - ((x - d)/c)^2 }

    we find that:
    > a = y3
    > b = y2 - y3
    > c = x3 - x2
    > d = x2

    flat_circular:
    ==============
    Inverse of steep circular for the two sides.

    """
    if curve == "spline":
        return lambda xx: interpolate.splev(
            xx, tck=interpolate.splrep(x, y, k=2)
        ).item()
    elif curve == "steep_circular":
        x1, x2, x3 = x
        y1, y2, y3 = y

        def _eval(x):
            if x < x2:
                return y1 - (y1 - y2) * sqrt(1 - ((x - x2) / (x2 - x1)) ** 2)
            elif x > x2:
                return y3 + (y2 - y3) * sqrt(1 - ((x - x2) / (x3 - x2)) ** 2)
            else:
                return y2

        return _eval
    elif curve == "flat_circular":
        x1, x2, x3 = x
        y1, y2, y3 = y

        def _eval(x):
            if x < x2:
                return y2 + (y1 - y2) * sqrt(1 - ((x - x1) / (x2 - x1)) ** 2)
            elif x > x2:
                return y2 - (y2 - y3) * sqrt(1 - ((x - x3) / (x3 - x2)) ** 2)
            else:
                return y2

        return _eval
    elif curve == "sigmoid":
        pass


def convert_odds_to_percent(odd, fro="percent"):
    if fro == "percent":
        return odd
    elif fro == "american":
        return 100.0 / (odd + 100.0) if odd >= 0 else (-odd) / (-odd + 100.0)
    elif fro == "decimal":
        return 1 / odd
    else:
        raise


def convert_odds_from_percent(odd, to="decimal"):
    if to == "percent":
        return odd
    elif to == "american":
        return (
            100.0 / odd - 100.0 if odd >= 0.5 else (-100.0 * odd) / (1.0 - odd)
        )
    elif to == "decimal":
        return 1.0 / odd
    else:
        raise


def convert_odds(odd, to="percent", fro="american"):
    return convert_odds_from_percent(convert_odds_to_percent(odd, fro), to)
