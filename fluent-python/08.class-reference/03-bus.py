#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import copy
# 校车乘客在途中上车和下车
class Bus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

    def __repr__(self):
        return str(self.passengers)


if __name__ == "__main__":
    bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
    bus2 = copy.copy(bus1)
    bus3 = copy.deepcopy(bus1)

    print("id(bus1), id(bus2), id(bus3): {}, {}, {}".format(id(bus1), id(bus2), id(bus3)))

    bus1.drop('Bill')
    print("bus1: {}".format(bus1))
    print("bus2: {}".format(bus2))

    print("id(bus1.passengers), id(bus2.passengers), id(bus3.passengers): {}, {}, {}".format(id(bus1.passengers), id(bus2.passengers), id(bus3.passengers)))
    print("bus3: {}".format(bus3))

    bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
    bus2 = Bus(['Alice', 'Bill', 'Claire', 'David'])
    bus3 = Bus(['Alice', 'Bill', 'Claire', 'David'])

    print("id(bus1), id(bus2), id(bus3): {}, {}, {}".format(id(bus1), id(bus2), id(bus3)))

    bus1.drop('Bill')
    print("bus1: {}".format(bus1))
    print("bus2: {}".format(bus2))

    print("id(bus1.passengers), id(bus2.passengers), id(bus3.passengers): {}, {}, {}".format(id(bus1.passengers), id(bus2.passengers), id(bus3.passengers)))
    print("bus3: {}".format(bus3))
