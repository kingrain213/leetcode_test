
import sys
import json
import os
import numpy as np
import time

"""
编写一个程序，找出第 n 个丑数。

丑数就是质因数只包含 2, 3, 5 的正整数。

示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
说明:  

1 是丑数。
n 不超过1690。

题解：
丑数要从小到大排序，设定三个指针初始化为数组里第一个数，每次三个指针乘以对应的因子，比较大小，把最小的append进去
对应索引+1
"""

def nthUglyNumber(n):
    idx2 = 0
    idx3 = 0
    idx5 = 0
    res = [1]
    for i in range(n-1):
        res.append(min(res[idx2]*2, res[idx3]*3, res[idx5]*5))
        if res[-1] == res[idx2] * 2:
            idx2 += 1
        if res[-1] == res[idx3] * 3:
            idx3 += 1
        if res[-1] == res[idx5] * 5:
            idx5 += 1
    
    return res[-1]


if __name__ == '__main__':
    
   
    num = 10
    t1 = time.time()
    output = nthUglyNumber(num)
    
    t2 = time.time()
    print('mathod 1:', output)
    #print('mathod 2:', output2)
    print ('timecost~~~~~~~~~~~~~:', t2-t1)
