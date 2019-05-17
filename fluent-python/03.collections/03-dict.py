#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, os, sys

BATCHPATH = os.path.dirname(os.path.dirname(os.path.abspath(os.path.realpath(__file__))))
sys.path.insert(0, BATCHPATH)

from lib.base import gettime, info, warn, error


if __name__ =='__main__':
    # ❶ 一个承载成对数据的列表， 它可以直接用在字典的构造方法中
    DIAL_CODES = [
                (86, 'China'),
                (91, 'India'),
                (1, 'United States'),
                (62, 'Indonesia'),
                (55, 'Brazil'),
                (92, 'Pakistan'),
                (880, 'Bangladesh'),
                (234, 'Nigeria'),
                (7, 'Russia'),
                (81, 'Japan'),
    ]

    # ❷ 这里把配好对的数据左右换了下， 国家名是键， 区域码是值
    country_code = {country: code for code, country in DIAL_CODES}
    info("country_code: %s" %(country_code))

    # ❸ 跟上面相反， 用区域码作为键， 国家名称转换为大写， 并且过滤掉区域码大于或等于 66 的地区
    country_code2 = {code: country.upper() for country, code in country_code.items() if code < 66}
    info("country_code2: %s" %(country_code2))

    country_code3 = {code: country.upper() for country, code in country_code.items() if code < 66 and country[0] in "IU"}
    info("country_code3: %s" %(country_code3))



