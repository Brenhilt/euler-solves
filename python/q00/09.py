# Python3, vim: set fileencoding=utf-8:
# Author  : Brenhilt Schildt <ver51+git@brenhilt.com>
# Created : 2019-07-12


def q0009():  # {{{
    """  {{{
    a^2 + b^2 = c^2, a + b + c = 1000 = t, a < b < c
    c = {t - (a + b)},
    a^2 + b^2 = {t - (a + b)}^2 = t^2 - 2t(a + b) + (a + b)^2
    t^2 - 2ta - 2tb + 2ab = 0, 2(t - a)b = t^2 - 2ta = t(t - 2a)
    b = t(t - 2a)/{2(t - a)}
    a < b, t(t - 2a)/{2(t - a)} - a > 0, t(t - 2a) - 2a(t - a) > 0,
    t^2 - 4ta + 2a^2 > 0, a^2 - 2ta +t^2 - (t^2)/2 > 0,
    (a - t)^2 - (t/sqrt(2))^2 > 0, a < t - t/sqrt(2) = t/sqrt(2)(sqrt(2) - 1)
    = t/(2 + sqrt(2))
    }}}"""
    max_a = 1000 / (2 + 2 ** 0.5)
    # for a in range(1, int(max_a) + 1):
    for a in range(int(max_a), 0, -1):
        b = 1000 * (500 - a) / (1000 - a)
        if b - int(b) == 0:
            return a * int(b) * (1000 - a - int(b))
# }}}


if __name__ == "__main__":  # {{{
    result = q0009()
    print(result)
# }}}
