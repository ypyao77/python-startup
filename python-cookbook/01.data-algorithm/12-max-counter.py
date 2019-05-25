#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 怎样找出一个序列中出现次数最多的元素呢
if __name__ == "__main__":
    # collections.Counter 类就是专门为这类问题而设计的，它甚至有一个有用的most_common() 方法直接给了你答案。
    # 为了演示，先假设你有一个单词列表并且想找出哪个单词出现频率最高
    words = [
            'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
            'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
            'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
            'my', 'eyes', "you're", 'under'
            ]

    from collections import Counter

    word_counts = Counter(words)
    # 出现频率最高的 3 个单词
    top_three = word_counts.most_common(3)
    print(top_three)

    # 作为输入， Counter 对象可以接受任意的由可哈希（ hashable）元素构成的序列
    # 对象。在底层实现上，一个 Counter 对象就是一个字典，将元素映射到它出现的次数上。
    print("word_counts['not']: ", word_counts['not'])
    print("word_counts['eyes']: ", word_counts['eyes'])

    # 手动增加计数，可以简单的用加法
    print("word_counts: ", word_counts)
    morewords = ['why','are','you','not','looking','in','my','eyes', "cc", "cc"]
    for word in morewords:
        word_counts[word] += 1

    print("word_counts: ", word_counts)
    print("word_counts['eyes']: ", word_counts['eyes'])

    word_counts.update(morewords)
    print("word_counts: ", word_counts)
    print("word_counts['eyes']: ", word_counts['eyes'])

    # Counter 实例一个鲜为人知的特性是它们可以很容易的跟数学运算操作相结合
    a = Counter(words)
    b = Counter(morewords)
    print("a: ", a)
    print("b: ", b)

    c = a + b
    d = a - b
    print("c: ", c)
    print("d: ", d)


