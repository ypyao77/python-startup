#!/usr/bin/python
#coding=utf8

class UserCollection:
 
    def __init__(self, users):
        self._users = users
 
    def __len__(self):
        return len(self._users)
 
 
user1, user2, user3 = UserCollection(['piglei', 'raymond']), UserCollection([]), UserCollection(None)
 
# 定义了 __len__ 方法后，UserCollection 对象本身就可以被用于布尔判断了
if user1:
    print("There's some users in user1!")
else:
    print("There's no user in user1!")

if user2:
    print("There's some users in user2!")
else:
    print("There's no user in user2!")

if user3:
    print("There's some users in user3!")
else:
    print("There's no user in user3!")

