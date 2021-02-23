
import sys
import json
import os
import numpy as np
import time

"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例 1：

输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。

示例 2：
输入：nums = [1]
输出：1

示例 3：
输入：nums = [0]
输出：0

示例 4：
输入：nums = [-1]
输出：-1

示例 5：
输入：nums = [-100000]
输出：-100000

类似于动态规划方案，统计子集的长度，当前子集的和等于前面的和加当前值，如果加上当前值大于当前值则累加，否则直接和是当前值
"""
def maxSubArray(nums):
    maxsum = nums[0]
    pre = nums[0]
    for i in range(1, len(nums)):
        pre = max(nums[i], pre+nums[i])
        maxsum = max(maxsum, pre)
        print('index {}, pre {}, maxsum {}'.format(i, pre, maxsum))
    return maxsum

if __name__ == '__main__':
    
   
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    nums = [1]
    nums = [0]
    t1 = time.time()
    output = maxSubArray(nums)
    
    t2 = time.time()
    print('mathod 1:', output)
    #print('mathod 2:', output2)
    print ('timecost~~~~~~~~~~~~~:', t2-t1)
