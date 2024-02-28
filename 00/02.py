# Python3, vim: set fileencoding=utf-8:
# Author  : Brenhilt Schildt <ver51+git@brenhilt.com>
# Created : 2019-07-10


def q0002():  # {{{
    res = 2
    a, b = 3, 5
    while a + b < 4000000:
        res += a + b
        a, b = a + 2 * b, 2 * a + 3 * b
    return res
# }}}


if __name__ == "__main__":  # {{{
    result = q0002()
    print(result, ed - st)
# }}}
