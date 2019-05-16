#!/usr/bin/env python
# -*- coding: utf-8 -*-

SUFFIXES = {
        1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
        1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']
}

def approximate_size(size, a_kilobyte_is_1024_bytes=True):
    '''Convert a file size to human‐readable form.
    Keyword arguments:
                        size ‐‐ file size in bytes
    a_kilobyte_is_1024_bytes ‐‐ if True (default), use multiples of 1024 if False, use multiples of 1000
    Returns: string
    '''
    if size < 0:
        raise ValueError('number must be non‐negative')

    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000

    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple:
            # {0:.1f} 包含了两方面的内容： {0}
            # 你已经能理解， :.1f 则不一定了。
            # 第二部分（包括冒号及其后边的部分）即格式说明符(format specifier)，
            # 它进一步定义了被替换的变量应该如何被格式化。
            # {1}会被传递给 format()方法的第二个参数替换，即 suffix。
            return '{0:.1f} {1}'.format(size, suffix)

    raise ValueError('number too large')
