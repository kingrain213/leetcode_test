import numpy as np
import json
import os
import sys

"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

 

示例 1：

输入：strs = ["flower","flow","flight"]
输出："fl"
示例 2：

输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。

方法1：从第一个字符串一直往后两两比较，中断为止
方法2：扫描每个字符串第一列，第二列，直到第N列不相同为止
#方法3：分治算法，把strs分成几组，每组内匹配，再组组间匹配
方法4：最小二分法，最小长度是minilen，先算minilen是否在每个数组，否则算minilen/2，否则再/4....

最好用二分法，V3和V4算法一致，V3比较笨，边界问题通过各个条件判断，最好用V4
"""  
def longestCommonPrefix_v1(strs:list):
    def find_same(str1, str2):
        if min(len(str1), len(str2)) == 0:
            return ""
        index = 0
        while index < min(len(str1), len(str2)) and str1[index] == str2[index]:
            index += 1
        return str1[:index]

    if len(strs) == 0:
        return ""
    prefix = strs[0]
    for i in range(1,len(strs)):
        prefix = find_same(prefix, strs[i])
        if not prefix:
            break
    return prefix

def longestCommonPrefix_v2(strs:list):
    if len(strs) == 0:
        return ""

    minlen = min(len(s) for s in strs)
    prefix = ""
    for i in range(minlen):
        prefix = strs[0][:i]
        if not all(s[:i] == prefix for s in strs):
            break
    return prefix[:-1]

def longestCommonPrefix_v3(strs:list):
    if not strs:
        return ''
    minlen = min(len(s) for s in strs)
    start = 0
    end = minlen
    while start < end:
        mid = (start + end + 1) >>1
        print (start, mid, end)
        prefix = strs[0][:mid]
        if all(prefix == strs[i][:mid] for i in range(0, len(strs))):
            start = mid
        else:
            end = mid - 1
    return strs[0][:start]

def longestCommonPrefix_v4(strs:list):
    if len(strs) == 0:
        return ""

    minlen = min(len(s) for s in strs)
    prefix = strs[0][:minlen]
    final = ''
    start = 0
    end = minlen
    mid = (start + end) >> 1
    while start <= end and prefix != final:
        mid = (start + end) >> 1
        print (start, end, mid)
        prefix = strs[0][:mid]
        if all(stemp[:mid] == prefix for stemp in strs):
            start = mid
            final = prefix
        else:
            end = mid - 1
            

    return final

if __name__ == '__main__':
    # strs = ["flower","flow","flight"]
    # strs = ['a']
    strs = ["dog","racecar","car"]
    result = longestCommonPrefix_v4(strs)
    print ("same prefix:", result)
    
