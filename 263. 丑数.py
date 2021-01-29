
import sys
import json
import os
import numpy as np
import time

"""
编写一个程序判断给定的数是否为丑数。

丑数就是只包含质因数 2, 3, 5 的正整数。

示例 1:
输入: 6
输出: true
解释: 6 = 2 × 3
示例 2:

输入: 8
输出: true
解释: 8 = 2 × 2 × 2
示例 3:

输入: 14
输出: false 
解释: 14 不是丑数，因为它包含了另外一个质因数 7。

题解：
动态规划或者累计除法一直分解下去变换自身值即可，注意边界和终止条件
"""

def isUgly(num):
    if num <= 0:
        return False
    while True:
        if num == 1 or num == 2 or num == 5:
            return True
        if num % 2 == 0:
            num /= 2
        elif num % 3 == 0:
            num /= 3
        elif num % 5 == 0:
            num /= 5
        else:
            return False


if __name__ == '__main__':
    
   
    num = 14
    t1 = time.time()
    output = isUgly(num)
    
    t2 = time.time()
    print('mathod 1:', output)
    #print('mathod 2:', output2)
    print ('timecost~~~~~~~~~~~~~:', t2-t1)
