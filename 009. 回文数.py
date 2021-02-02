
import sys
import json
import os
import numpy as np
import time

"""
给你一个整数 x ，如果 x 是一个回文整数，返回 ture ；否则，返回 false 。

回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。

 
示例 1：
输入：x = 121
输出：true

示例 2：
输入：x = -121
输出：false
解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

示例 3：
输入：x = 10
输出：false
解释：从右向左读, 为 01 。因此它不是一个回文数。

示例 4：
输入：x = -101
输出：false
 

提示：

-231 <= x <= 231 - 1
 

进阶：你能不将整数转为字符串来解决这个问题吗？

题解：
1）转换成字符串判断对称性，需要耗费O(N)的内存
2）颠倒后判断是否相等，可能越界
3）所以翻转一半数字，考虑是否相等
"""
def isPalindrome(x):
    """
    特殊情况，如果x < 0 ,则 -1 ！= 1-
    如果x > 0 且末位是0 则 20 ！= 02
    单独的0属于回文数字
    """
    if x < 0 or (x > 0 and x % 10 == 0):
        return False
    revert = 0
    while x > revert:
        revert = revert * 10 + x % 10
        x = x /10
    """
    如果数字长度为偶数时，如：1221，最后两位21反转后成12，与前两位相当，x == revert
    如果数字长度为奇数数，如: 12321,最后三位反转后，变成123，需要除以10去掉最后一位
    """
    if revert == x or x == revert / 10:
        return True

    return False

if __name__ == '__main__':
    
   
    num = 121
    t1 = time.time()
    output = isPalindrome(num)
    
    t2 = time.time()
    print('mathod 1:', output)
    #print('mathod 2:', output2)
    print ('timecost~~~~~~~~~~~~~:', t2-t1)
