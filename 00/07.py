# Python3, vim: set fileencoding=utf-8:
# Author  : Brenhilt Schildt <ver51+git@brenhilt.com>
# Created : 2019-07-12


def q0007():  # {{{
    from math import log
    n = 10001
    sup = int(n * (log(n) + log(log(n))))
    l = len(range(3, sup, 2))
    pt = [True] * l
    for i in range(l):
        if pt[i]:
            s = 2 * i + 3
            for j in range(i + s, l, s):
                pt[j] = False
    p = [i for i in range(len(pt)) if pt[i]]
    return p[10000]
# }}}


if __name__ == "__main__":  # {{{
    result = q0007()
    print(result)
# }}}
