import sys
import json
import os
import numpy as np
import time
import operator

"""
给出 n 个数对。 在每一个数对中，第一个数字总是比第二个数字小。
现在，我们定义一种跟随关系，当且仅当 b < c 时，数对(c, d) 才可以跟在 (a, b) 后面。我们用这种形式来构造一个数对链。
给定一个数对集合，找出能够形成的最长数对链的长度。你不需要用到所有的数对，你可以以任何顺序选择其中的一些数对来构造。

示例：
输入：[[1,2], [2,3], [3,4]]
输出：2
解释：最长的数对链是 [1,2] -> [3,4]

方法1：
要求第二对的x大于第一对的y，自身又满足y > x
按照第二位升序排序，已经升序，所以第一个数肯定在里面
[(x1,y1), (x2,y2), (x3,y3)...(xn,yn)]
方法2：
todo 动态规划
"""

def findLongestChain(pairs):
    ans = 0
    cur = float('-inf')
    for x, y in sorted(pairs, key=operator.itemgetter(1)):
        if cur < x: #后一对的第一位大于前一对的第二位
            cur = y
            ans += 1
        print (x,y)
    return ans

if __name__ == '__main__':
    input = [[1,5], [2,3], [3,4]]
    t1 = time.time()
    output = findLongestChain(input)
    t2 = time.time()
    print(output)
    print ('timeout:', t2-t1)
