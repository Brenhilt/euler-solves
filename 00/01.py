# Python3, vim: set fileencoding=utf-8:
#
# Author  : Brenhilt Schildt <ver51+git@brenhilt.com>
# Created : 2019-07-10


def q0001():  # {{{
    return sum([i for i in range(1, 1001) if (i % 3) * (i % 5) == 0])
# }}}


if __name__ == "__main__":  # {{{
    result = q0001()
    print(result)
# }}}
