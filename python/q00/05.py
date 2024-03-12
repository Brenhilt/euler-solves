# Python3, vim: set fileencoding=utf-8:
# Author  : Brenhilt Schildt <ver51+git@brenhilt.com>
# Created : 2019-07-11


def q0005():  # {{{
    p = 2 * 3
    for i in range(4, 21):
        d, n = p, i
        while n > 0:
            d, n = n, d % n
        p = p * i // d
    return p
# }}}


if __name__ == "__main__":  # {{{
    result = q0005()
    print(result)
# }}}
