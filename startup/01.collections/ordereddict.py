from collections import OrderedDict


class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)


od = LastUpdatedOrderedDict(5)
od['z'] = "z"
od['y'] = "y"
od['x'] = "x"
od['w'] = "w"
od['v'] = "v"
od['u'] = "u"
od['t'] = "t"
od['s'] = "s"
od['r'] = "r"

print("od = {0}".format(od))

