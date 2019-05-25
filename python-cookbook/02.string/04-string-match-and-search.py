#!/usr/bin/env python3


# 字符串匹配和搜索
# 你想匹配或者搜索特定模式的文本
if __name__ == "__main__":
    # 如果你想匹配的是字面字符串，那么你通常只需要调用基本字符串方法就行，比如str.find() , str.endswith() , str.startswith() 或者类似的方法：
    text = 'yeah, but no, but yeah, but no, but yeah'
    print("text == 'yeah': ", text == 'yeah')
    print("text.startswith('yeah'): ", text.startswith('yeah'))
    print("text.endswith('no'): ", text.endswith('no'))
    print("text.find('no'): ", text.find('no'))


    # 对于复杂的匹配需要使用正则表达式和 re 模块。为了解释正则表达式的基本原理，
    # 假设你想匹配数字格式的日期字符串比如 11/27/2012 ，你可以这样做
    text1 = '11/27/2012'
    text2 = 'Nov 27, 2012'

    import re
    # Simple matching: \d+ means match one or more digits
    if re.match(r'\d+/\d+/\d+', text1):
        print('yes')
    else:
        print('no')

    if re.match(r'\d+/\d+/\d+', text2):
        print('yes')
    else:
        print('no')

    # 如果你想使用同一个模式去做多次匹配，你应该先将模式字符串预编译为模式对象。
    datepat = re.compile(r'\d+/\d+/\d+')
    if re.match(datepat, text1):
        print('yes')
    else:
        print('no')

    if re.match(datepat, text2):
        print('yes')
    else:
        print('no')

    text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
    print("text: ", text)
    print("datepat.findall(text): ", datepat.findall(text))

    # 在定义正则式的时候，通常会利用括号去捕获分组
    # datepat = re.compile(r'(\d+)/(\d+)/(\d+)')

    # 捕获分组可以使得后面的处理更加简单，因为可以分别将每个组的内容提取出来
    datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
    m = datepat.match('11/27/2012')
    print("m: ", m)

    print("m.group(0): ",  m.group(0))
    print("m.group(1): ",  m.group(1))
    print("m.group(2): ",  m.group(2))
    print("m.group(3): ",  m.group(3))
    print("m.groups: ",  m.groups)

    month, day, year = m.groups()
    print("month, day, year: ", month, day, year)

    print("text: ", text)
    print("datepat.findall(text): ", datepat.findall(text))

    for month, day, year in datepat.findall(text):
        print('{}-{}-{}'.format(year, month, day))

    # findall() 方法会搜索文本并以列表形式返回所有的匹配。如果你想以迭代方式返回匹配，可以使用 finditer() 方法来代替
    for m in datepat.finditer(text):
        print(m.groups())

    # 讨论: 关于正则表达式理论的教程已经超出了本书的范围。不过，这一节阐述了使用 re
    # 模块进行匹配和搜索文本的最基本方法。核心步骤就是先使用 re.compile() 编译正则
    # 表达式字符串，然后使用 match() , findall() 或者 finditer() 等方法。
    m = datepat.match('11/27/2012abcdef')
    print("m.group(): ", m.group())

    # 如果你想精确匹配，确保你的正则表达式以 $ 结尾
    datepat = re.compile(r'(\d+)/(\d+)/(\d+)$')
    m = datepat.match('11/27/2012abcdef')
    try:
        print("m.group(): ", m.group())
    except Exception as e:
        print(e)
    m = datepat.match('11/27/2012')
    print("m.group(): ", m.group())

    # 如果你仅仅是做一次简单的文本匹配/搜索操作的话，可以略过编译部分，直接使用 re 模块级别的函数。
    m = re.findall(r'(\d+)/(\d+)/(\d+)', text)
    print("m.group(): ", m.group())

    # 需要注意的是，如果你打算做大量的匹配和搜索操作的话，最好先编译正则表达式，
    # 然后再重复使用它。模块级别的函数会将最近编译过的模式缓存起来，因此并不
    # 会消耗太多的性能，但是如果使用预编译模式的话，你将会减少查找和一些额外的处理损耗



