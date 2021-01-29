
import sys
import json
import os
import numpy as np
import time

"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。


示例 1：
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]

示例 2：
输入：nums = []
输出：[]

示例 3：
输入：nums = [0]
输出：[]


题解：
考虑到不重复，不能先查找候选集后再排序和去重，所以在查找前
1）暴力遍历：三重循环，保证当前循环数不等于上一个数字，就不会出现重复的，复杂的O(N3)
2）优化成两个循环：循环加双指针，外层循环继续，内层循环second从左到右，third从右到左，考虑到a + b + c = 0
    固定a，b往右变大了，c肯定往左变小了
"""

def threeSum(nums):
    nums.sort()
    result = []
    for first in range(len(nums)):
        if first == 0 or nums[first] != nums[first-1]:
            for second in range(first+1, len(nums)):
                if second == first+1 or nums[second] != nums[second-1]:
                    for third in range(second+1, len(nums)):
                        if third == second + 1 or nums[third] != nums[third-1]:
                            if nums[first] + nums[second] + nums[third] == 0:
                                result.append([nums[first], nums[second], nums[third]])
    return result

def threeSum_v2(nums):
    nums.sort() #数组先进行排序，遇到相同数字则continue
    n = len(nums)
    result = []
    for first in range(n):
        #需要和上一次枚举的数不同
        if first > 0 and nums[first] == nums[first - 1]: 
            continue
        third = n - 1
        target = -nums[first]
        #第二层循环逐渐右移增大，所以第三层循环逐渐左移减小即可
        #第二层变量逐渐增大，第三层固定变量，自身减小左移即可
        for second in range(first+1, n):
            if second > first + 1 and nums[second] == nums[second - 1]:
                continue
            #需要保证second在third的左侧
            while second < third and nums[second] + nums[third] > target:
                third -= 1
            #如果指针合并，随着b后续增加，就不会有a+b+c = 0 并且b < c
            #跳出整个第二层循环，继续下次的first大循环
            if second == third:
                break
            #上面找到third后，此处只运算一次，while语句 < 或者 == 等停止，等于则满足条件，小于则进行下一次循环
            if nums[first] + nums[second] + nums[third] == 0:
                result.append([nums[first], nums[second], nums[third]])
    return result


if __name__ == '__main__':
    
    input = [-1,0,1,2,-1,-4]
    # input = []
    # input = [0]
    
    t1 = time.time()
    output = threeSum(input)
    output2 = threeSum_v2(input)
    t2 = time.time()
    print('mathod 1:', output)
    print('mathod 2:', output2)
    print ('timecost~~~~~~~~~~~~~:', t2-t1)
