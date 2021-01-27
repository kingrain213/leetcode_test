
import sys
import json
import os
import numpy as np
import time
import operator
import cv2

"""
升序排列的整数数组 nums 在预先未知的某个点上进行了旋转（例如， [0,1,2,4,5,6,7] 经旋转后可能变为 [4,5,6,7,0,1,2] ）。
请你在数组中搜索 target ，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
 

示例 1：
输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4

示例 2：
输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1

示例 3：
输入：nums = [1], target = 0
输出：-1

题解：
1）最暴力的是循环，复杂度O(n),太高
2）最快的是二分查找，毕竟是有序数组，从mid处断开，肯定左右两侧有一侧是顺序的
    if  左侧有序，判断target在左侧left到mid之间，则right改到mid，查找(left,mid-1)
                 否则left改为mid，查找(mid+1, right)
    else右侧有序，判断target在右侧mid和right之间，则left改为mid，查找(mid+1, right)
                 否则right改为mid，查找(left,mid-1)

基本思路是二分，肯定某一边是有序的，判断target是否在有序数组内，在的话，调整left、right
到该区间，否则调整到另外一半

一定要注意每次循环封闭条件
"""
def search(nums:list, target):
    left = 0
    right = len(nums) - 1
    index = -1
    while left <= right:
        mid = (left + right) >> 1
        if nums[mid] == target:
            index = mid
            break
        if nums[left] <= nums[mid]: #计算mid时本来就有四舍五入的情况，所以要把等号放在此处
            if nums[left] <= target and target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target and target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return index

if __name__ == '__main__':
    
    input = [3, 1]
    target = 1#0
    t1 = time.time()
    output = search(input, target)
    t2 = time.time()
    print(output)
    print ('timecost~~~~~~~~~~~~~:', t2-t1)
