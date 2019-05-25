#!/usr/bin/env python3


# 字符串开头或结尾匹配
# 你需要通过指定的文本模式去检查字符串的开头或者结尾，比如文件名后缀， URL Scheme 等等
if __name__ == "__main__":
    # 检查字符串开头或结尾的一个简单方法是使用 str.startswith() 或者是 str.endswith() 方法
    filename = 'spam.txt'
    print("filename: ", filename)
    print("filename.endswith('.txt'): ", filename.endswith('.txt'))
    print("filename.startswith('file:'): ", filename.startswith('file:'))

    url = 'http://www.python.org'
    print("url: ", url)
    print("url.startswith('http:'): ", url.startswith('http:'))

    # 如果你想检查多种匹配可能，只需要将所有的匹配项放入到一个元组中去，然后传给 startswith() 或者 endswith() 方法
    filenames = ["watch.c", "inc.h", "run.py", "run.sh", "run.c", "main.c", "main.cpp"]
    print("filenames: ", filenames)
    print("[name for name in filenames if name.endswith(('.c', '.h')) ]: ", [name for name in filenames if name.endswith(('.c', '.h')) ])
    print("any(name.endswith('.py') for name in filenames): ", any(name.endswith('.py') for name in filenames))

    # 这个方法中必须要输入一个元组作为参数。如果你恰巧有一个 list 或者 set 类型的选择项，要确保传递参数前先调用 tuple() 将其转换为元组类型
    choices = ['http:', 'ftp:']
    url = 'http://www.python.org'
    print("choices: ", choices)
    print("url: ", url)
    try:
        print("url.startswith(choices): ", url.startswith(choices))
    except Exception as e:
        print(e)
    print("url.startswith(tuple(choices)): ", url.startswith(tuple(choices)))

    # startswith() 和 endswith() 方法提供了一个非常方便的方式去做字符串开头和
    # 结尾的检查。类似的操作也可以使用切片来实现，但是代码看起来没有那么优雅。
    filename = 'spam.txt'
    filename[-4:] == '.txt'
    url = 'http://www.python.org'
    url[:5] == 'http:' or url[:6] == 'https:' or url[:4] == 'ftp:'

    # 你可以能还想使用正则表达式去实现
    import re
    url = 'http://www.python.org'
    print("url: ", url)
    print(re.match('http:|https:|ftp:', url))

    # 最后提一下，当和其他操作比如普通数据聚合相结合的时候 startswith() 和
    # endswith() 方法是很不错的。比如，下面这个语句检查某个文件夹中是否存在指定的
    # 文件类型
    # if any(name.endswith(('.c', '.h')) for name in listdir(dirname)):
    #









