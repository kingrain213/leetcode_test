"""
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。
示例1：
输入："abc"
输出：3
解释：三个回文子串: "a", "b", "c"
示例2：
输入："aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"

解析：
最笨的方法：暴力遍历发
1）罗列所有字符子串，判断每个子串是否为回文串
2）罗列字符串中心
  a)回文字符串长度可以是奇数或者偶数，奇数时，左质心右质心都是i(长度为n)，偶数时，左质心为i,右质心为i+1,长度为n-1，所以共有2*n-1个质心
  b)以当前质心为中心，左右扩张，左侧==右侧时，回文数加1，然后左质心坐标--，右质心坐标++，直到左侧小于0或者右侧>= n或者左侧!=右侧了终止
3）todo mancher优化算法(暂未看懂)
"""

import sys
import json
import os
import numpy as np
import time

def countSubstrings(s):
    n = len(s)
    size = n * 2 - 1
    ans = 0
    for  i in range(size):
        l = i // 2
        r = i // 2 + i%2
        while l >= 0 and r < n and s[l] == s[r]:
            ans += 1
            l -= 1
            r += 1
    return ans

if __name__ == '__main__':
    input = "abc"
    t1 = time.time()
    output = countSubstrings(input)
    t2 = time.time()
    print(output)
    print ('timeout:', t2-t1)
