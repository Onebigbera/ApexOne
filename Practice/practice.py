# -*-coding:utf-8 -*-
"""
    practice
"""


def say(*args):
    """
    在参数中使用*args，在函数中使用args会合包为元组
    在参数中使用*args，在函数中使用*args会原样展示

    :param args:
    :return:
    """
    print(args)
    print(*args)


def action(args):
    """
    在参数中使用args，在函数中使用*args会对参数进行解包
    :param args:
    :return:
    """
    print(*args)


if __name__ == "__main__":
    string = [1, 2, 3, 4, 5]
    say(1, 2, string)

    args = (1, 2, 3, 4, 5)
    action(args)
