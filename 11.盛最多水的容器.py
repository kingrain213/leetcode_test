"""
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器。

示例 1：



输入：[1,8,6,2,5,4,8,3,7]
输出：49 
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
示例 2：

输入：height = [1,1]
输出：1
示例 3：

输入：height = [4,3,2,1,4]
输出：16
示例 4：

输入：height = [1,2,1]
输出：2

解题方法：
面积 = 底边长度 * min(左边，右边)
采用双指针方法，左边和右边，向中间移动较小点的指针，底边也自减一
"""
import sys
import json
import os
import numpy as np
import time
import operator

def maxArea(height:list) -> int:
    left = 0
    right = len(height)-1
    size = len(height) - 1
    maxarea = size*min(height[left], height[right])
    while left < right:
        size -= 1
        if height[left] >= height[right]:
            right -= 1
        else:
            left += 1
        maxarea = max(maxarea, size*min(height[left], height[right]))
    return maxarea

if __name__ == '__main__':
    input = [1,8,6,2,5,4,8,3,7]
    t1 = time.time()
    output = maxArea(input)
    t2 = time.time()
    print(output)
    print ('timeout:', t2-t1)
