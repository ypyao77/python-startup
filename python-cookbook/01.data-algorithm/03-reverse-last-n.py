#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 保留有限历史记录正是 collections.deque 大显身手的时候。比如，下面的代码
# 在多行上面做简单的文本匹配，并返回匹配所在行的最后 N 行
import sys
from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)

    for line in lines:
        if pattern in line:
            yield line, previous_lines

        previous_lines.append(line)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.exit(1)

    with open(sys.argv[1]) as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')

        print(line, end='')
        print('-' * 20)

