#!/usr/bin/env python3

# 合并多个字典或映射
if __name__ == "__main__":
    # 现在有多个字典或者映射，你想将它们从逻辑上合并为一个单一的映射后执行某
    # 些操作，比如查找值或者检查某些键是否存在
    a = {'x': 1, 'z': 3 }
    b = {'y': 2, 'z': 4 }

    # 现在假设你必须在两个字典中执行查找操作（比如先从 a 中找，如果找不到再在 b
    # 中找）。一个非常简单的解决方案就是使用 collections 模块中的 ChainMap 类。
    from collections import ChainMap
    c = ChainMap(a,b)
    print(c['x']) # Outputs 1 (from a)
    print(c['y']) # Outputs 2 (from b)
    print(c['z']) # Outputs 3 (from a)

    # 对于字典的更新或删除操作总是影响的是列表中第一个字典
    c['z'] = 10
    c['w'] = 40
    print(c)
    print(a)
    print(b)

    try:
        del c['y']
    except Exception as e:
        print(e)


    a = {'x': 1, 'z': 3 }
    b = {'y': 2, 'z': 4 }
    merged = ChainMap(a, b)
    print("merged: ", merged)
    a['x'] = 42
    print("merged: ", merged)
    merged['x'] = 33
    print("merged: ", merged)
    b['y'] = 12
    print("merged: ", merged)











