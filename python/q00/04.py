# Python3, vim: set fileencoding=utf-8:
# Author  : Brenhilt Schildt <ver51+git@brenhilt.com>
# Created : 2019-07-11


def q0004():  # {{{
    pal = 10101
    m = 10 ** 3
    a = m - 1
    while pal // a < m:
        for b in range(m - 1, a - 1, -1):
            n = a * b
            v = str(n)
            l = len(v) // 2
            if v[:l][::-1] == v[(-1) * l:] and pal < n:
                pal = n
                break
        a -= 1
    return pal
# }}}


if __name__ == "__main__":  # {{{
    result = q0004()
    print(result)
# }}}
