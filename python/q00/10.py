# Python3, vim: set fileencoding=utf-8:
# Author  : Brenhilt Schildt <ver51+git@brenhilt.com>
# Created : 2019-07-12


def q0010():  # {{{
    sup = 2 * 10 ** 6
    pt = [False, False] + [True] * (sup - 1)
    for i in range(2, sup):
        if pt[i]:
            for n in range(2, sup // i + 1):
                pt[i * n] = False
    return sum([i for i in range(sup) if pt[i]])
# }}}


if __name__ == "__main__":  # {{{
    result = q0010()
    print(result)
# }}}
