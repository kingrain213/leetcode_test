
import sys
import json
import os
import numpy as np
import time
import operator

"""
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
进阶：你可以设计并实现时间复杂度为 O(n) 的解决方案吗？

示例 1：
输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。

示例 2：
输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9

题解：
1）暴力方法：对于每一个x，遍历 x+1 x+2 x+3 一直到x + y是否都在数组num内，如果在的话长度为y + 1，接下来继续遍历第二个数，直至第n个数
2）优化：x+1的长度肯定比x的长度小1，所以统计当前数x时，先判断x-1是否在数组内，在的话，就没必要继续运算了
3）动态规划+hash,hash
"""

def longestConsecutive(nums:list) -> int:
    longest = 1
    nums_set = set(nums)
    for x in nums_set:
        if x - 1 not in nums_set:
            current = x
            cur_len = 1
            while current + 1 in nums_set:
                current += 1
                cur_len += 1
            longest = max(longest, cur_len)

    return longest

def search_v2(nums):
    hash_dict = dict()
    maxlength = 0

    for num in nums:
        if num not in hash_dict:
            left = hash_dict.get(num-1, 0)
            right = hash_dict.get(num+1, 0)
            curlength = left + right + 1
            maxlength = max(curlength, maxlength)

            hash_dict[num] = curlength
            hash_dict[num-left] = curlength
            hash_dict[num+right] = curlength
    return maxlength

if __name__ == '__main__':
    
    input = [100,4,200,1,3,2]
    #input = [0,3,7,2,5,8,4,6,0,1]
    
    t1 = time.time()
    output = longestConsecutive(input)
    output2 = search_v2(input)
    t2 = time.time()
    print(output, output2)
    print ('timecost~~~~~~~~~~~~~:', t2-t1)
