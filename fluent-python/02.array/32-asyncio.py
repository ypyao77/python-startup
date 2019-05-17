#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import time, os, sys

def gettime():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

def log(level, msg):
    try:
        raise Exception
    except:
        f = sys.exc_info()[2].tb_frame.f_back.f_back

    print("(%s) (%s) (%s-%s:%s %s) %s" %(gettime(), level, os.getpid(), os.path.basename(f.f_code.co_filename), str(f.f_lineno), f.f_code.co_name, msg))
    return

def info(msg):
    log("\033[34m\033[1mINFO\033[0m", msg)
    return

def warn(msg):
    log("\033[33m\033[1mWARN\033[0m", msg)
    return

def error(msg):
    log("\033[31m\033[1mERRO\033[0m", msg)
    return

def hello():
    time.sleep(1)

def run():
    for i in range(5):
        hello()
        info("hello world")

if __name__ == '__main__':
    info("go")
    run()
    info("done")

