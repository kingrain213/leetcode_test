
import sys
import json
import os
import numpy as np
import time

"""
给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。

 

进阶：你能否实现线性时间复杂度、仅使用额外常数空间的算法解决此问题?
 

示例 1：
输入：nums = [3,0,1]
输出：2
解释：n = 3，因为有 3 个数字，所以所有的数字都在范围 [0,3] 内。2 是丢失的数字，因为它没有出现在 nums 中。

示例 2：
输入：nums = [0,1]
输出：2
解释：n = 2，因为有 2 个数字，所以所有的数字都在范围 [0,2] 内。2 是丢失的数字，因为它没有出现在 nums 中。

示例 3：
输入：nums = [9,6,4,2,3,5,7,0,1]
输出：8
解释：n = 9，因为有 9 个数字，所以所有的数字都在范围 [0,9] 内。8 是丢失的数字，因为它没有出现在 nums 中。

示例 4：
输入：nums = [0]
输出：1
解释：n = 1，因为有 1 个数字，所以所有的数字都在范围 [0,1] 内。1 是丢失的数字，因为它没有出现在 nums 中。


题解：
1）排序：升序之后，判断nums[i] ?= i,不等的话则缺失该数字
2）for循环，每个数累计求和，叠加后n*(a1+an)/2 减去和即为缺失数字
3）按位与，一个数与自己为0，数组里面的数每个都与一下i和nums[i]剩下的便是缺失数字
"""

def missingNumber(nums):
    
    lost = 0
    for index, val in enumerate(nums):
        lost ^= index
        lost ^= nums[index]
    lost ^= len(nums)
    
    return lost


if __name__ == '__main__':
    
   
    num = [0,1]
    t1 = time.time()
    output = missingNumber(num)
    
    t2 = time.time()
    print('mathod 1:', output)
    #print('mathod 2:', output2)
    print ('timecost~~~~~~~~~~~~~:', t2-t1)
