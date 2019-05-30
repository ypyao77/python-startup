#!/usr/bin/env python3

# 13.14 限制内存和 CPU 的使用量

import signal
import resource
import os

# 你想对在 Unix 系统上面运行的程序设置内存或 CPU 的使用限制。

# resource 模块能同时执行这两个任务。

def time_exceeded(signo, frame):
    print("Time's up!")
    raise SystemExit(1)

def set_max_runtime(seconds):
    # Install the signal handler and set a resource limit
    soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
    resource.setrlimit(resource.RLIMIT_CPU, (seconds, hard))
    # 程序运行时， SIGXCPU 信号在时间过期时被生成，然后执行清理并退出。
    signal.signal(signal.SIGXCPU, time_exceeded)

def limit_memory(maxsize):
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    resource.setrlimit(resource.RLIMIT_AS, (maxsize, hard))


if __name__ == '__main__':
    set_max_runtime(15)
    while True:
        pass

    limit_memory(1024*12)
    l = []
    for j in range(1024):
        l.append("%s-%s" %(j, "-".join([str(x) for x in list(range(128))])))
    # should raise MemoryError


