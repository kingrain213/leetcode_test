
import sys
import json
import os
import numpy as np
import time
from functools import reduce

"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:
输入: [2,2,1]
输出: 1

示例 2:
输入: [4,1,2,1,2]
输出: 4

题解：
1）暴力匹配法，循环整个数组存入hash表中，最后统计dict中每个key出现的次数
2）暴力匹配法，set(list)去重后，求和二倍减去原数组，就是出现一次的数字
3）异或特性：数字异或自己为0，异或0为自己，异或具有交换律
"""

def singleNumber(nums:list) -> int:
    result = 0
    for num in nums:
        result ^= num
    return result

def singleNumber_v2(nums:list) -> int:
    return reduce(lambda x,y : x^y, nums)

if __name__ == '__main__':
    
    input = [2,2,1]
    #input = [0,3,7,2,5,8,4,6,0,1]
    
    t1 = time.time()
    output = singleNumber(input)
    output2 = singleNumber_v2(input)
    t2 = time.time()
    print(output, output2)
    print ('timecost~~~~~~~~~~~~~:', t2-t1)
