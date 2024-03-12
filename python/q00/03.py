# Python3, vim: set fileencoding=utf-8:
# Author  : Brenhilt Schildt <ver51+git@brenhilt.com>
# Created : 2019-07-11


def get_one_of_factor(n, st):  # {{{
    while st ** 2 < n:
        if n % st == 0:
            return (st, n // st,)
        st += 2
    return (-1, n,)
# }}}


def q0003():  # {{{

    t = 600851475143
    fs = list()
    st = 3
    f, nt = get_one_of_factor(t, st)
    while f != -1:
        t = nt
        st = f
        fs += [f]
        f, nt = get_one_of_factor(t, st)
    return nt
# }}}


if __name__ == "__main__":  # {{{
    result = q0003()
    print(result)
# }}}
