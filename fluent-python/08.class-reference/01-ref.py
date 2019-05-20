#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# charles 和 lewis 指代同一个对象

if __name__ == "__main__":
    charles = {'name': 'Charles L. Dodgson', 'born': 1832}
    lewis = charles

    print("id(charles), id(lewis): %s, %s" %(id(charles), id(lewis)))

    print("lewis is charles: %s" %(lewis is charles))
    print("lewis == charles: %s" %(lewis == charles))

    lewis['balance'] = 950
    print("charles: %s" %(charles))

    alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}

    print("id(charles), id(lewis), id(alex): %s, %s, %s" %(id(charles), id(lewis), id(alex)))
    print("alex == charles: %s" %(alex == charles))
    print("alex is not charles: %s" %(alex is not charles))

    mike = {'balance': 950, 'name': 'Charles L. Dodgson', 'born': 1832}
    print("mike == charles: %s" %(mike == charles))
