#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re


def build_match_and_apply_functions(pattern, search, replace):
    def matches_rule(word):
        return re.search(pattern, word)

    def apply_rule(word):
        return re.sub(search, replace, word)

    return (matches_rule, apply_rule)

rules = []
with open('plural4‐rules.txt', encoding='utf‐8') as pattern_file:
    for line in pattern_file:
        pattern, search, replace = line.split(None, 3)
        rules.append(build_match_and_apply_functions(pattern, search, replace))

def plural(noun):
    for matches_rule, apply_rule in rules:
        if matches_rule(noun):
            return apply_rule(noun)


if __name__ == "__main__":
    print("plural('match'): {0}".format(plural('match')))
    print("plural('bus'): {0}".format(plural('bus')))
    print("plural('ship'): {0}".format(plural('ship')))
    print("plural('sheep'): {0}".format(plural('sheep')))
    print("plural('goat'): {0}".format(plural('goat')))
    print("plural('biz'): {0}".format(plural('biz')))
    print("plural('school'): {0}".format(plural('school')))
