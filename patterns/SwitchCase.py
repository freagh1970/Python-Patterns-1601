# -*- coding: utf-8 -*-

def step_1():
    return 1


def step_2():
    return 2


def step_3():
    return 3


def step_4():
    return 4


def default():
    return 0


switcher = {
    1: step_1,
    2: step_2,
    3: step_3,
    4: step_4,
}


def switch(step):
    return switcher.get(step, default)()


print(switch(1))
print(switch(4))
