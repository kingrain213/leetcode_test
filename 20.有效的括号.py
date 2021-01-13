"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

思路：
    考虑入栈的思想，后进先出，最后遇到的左括号，应该先匹配
    遍历字符串，如果左括号，进栈，如果右括号，看看是否与最后一个进去的左括号匹配，配的话pop出来最后一个继续配
    不配的话，直接返回False

"""
import sys
import json
import os
import numpy as np
import time
import operator

def isValid(s):
    if len(s) % 2 == 1:
        return False
    sign = {
        '}' : '{',
        ']' : '[',
        ')' : '('
    }
    stack = []
    for temp in s:
        #如果右括号的话找左括号去匹配，配不上则失败，配上的话，则把stack中的左括号pop出来
        if temp in sign.keys():
            if not stack or sign[temp] != stack[-1]:
               return False
            stack.pop() #记得最后以为匹配之后要pop出来
        #如果是左括号，直接进栈
        else:
            stack.append(temp)
    #最后不能直接return True，还要看stack是否匹配成功清空了
    return not stack

if __name__ == '__main__':
    input = "{[]}"
    t1 = time.time()
    output = isValid(input)
    t2 = time.time()
    print(output)
    print ('timeout:', t2-t1)
