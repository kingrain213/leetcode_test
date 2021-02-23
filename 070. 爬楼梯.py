
import sys
import json
import os
import numpy as np
import time

"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。

示例 1：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶

示例 2：
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/climbing-stairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

动态规划:因为每次可以上一阶或者两阶楼梯，所以当前台阶可以是上一阶+1，或者上上阶+2，总步数等于
fn = fn-1 + fn-2
方法1：
采用数组存储每一步的方法次数，空间复杂度浪费为O(N)
方法2：
当前值只与前两个值相关，只保存，循环替代前两个值即可，节省空间复杂度
"""
def climbStairs_v1(n):
    steps = [1, 2]
    if n <= 2:
        return steps[n-1]
    for i in range(3, n+1):
        steps.append(steps[i-2] + steps[i-3])
        print (i, steps[i-2], steps[i-3], steps[-1])
    return steps[-1]

def climbStairs(n):
    pre = 0
    ppre = 0
    cur = 1
    for i in range(1, n+1):
        ppre = pre
        pre = cur
        cur = ppre + pre
    return cur

if __name__ == '__main__':
    
   
    nums = 2
    t1 = time.time()
    output = climbStairs(nums)
    
    t2 = time.time()
    print('mathod 1:', output)
    #print('mathod 2:', output2)
    print ('timecost~~~~~~~~~~~~~:', t2-t1)
