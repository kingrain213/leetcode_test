#coding:utf-8

'''
请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/daily-temperatures
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import sys
import json
import os
import numpy as np
import time

#暴力匹配法1，双重循环
#时间复杂度是O(n*n)
def dailyTemperatures(T:list) ->list:
    result = []

    for i in range(len(T)):
        sign = 0
        for j in range(i+1, len(T)):
            if T[j] > T[i]:
                sign = j-i
                break
        result.append(sign)
    return result

#暴力匹配2
#倒数去找，温度值是有限的，建key，每遍历一个值，更新对应的index查找比当前温度高的所有key对应的index，取最小index即可
def dailyTemperatures2(T:list) ->list:
    print(type(T))
    n = len(T)
    ans, nxt, big = [0]*n, dict(), 10**9
    for i in range(n-1, -1, -1):
        warmindex = min(nxt.get(t, big) for t in range(T[i]+1, 102))
        if warmindex != big:
            ans[i] = warmindex -i
        nxt[T[i]] = i
    return ans

#维护一个栈存储T的下标，0是栈底，n是栈顶，从栈底到栈顶对应温度逐渐减小
#新来一个温度，从栈顶开始匹配，如果比栈顶低，进栈
#如果比栈顶高，栈顶pop出来对应index，并且赋值对应天数为当前i - stack[-1]，栈继续朝底部遍历
#直到栈为空，或者当前温度小于栈内温度终止
#####注意当前值一定要入栈，否则初始条件都进不来，一直为错
def dailyTemperatures3(T:list) -> list:
    ans = len(T) * [0]
    stack = []
    for i in range(len(T)):
        while stack and T[stack[-1]] < T[i]:
            preindex = stack[-1]
            ans[preindex] = i - preindex
            stack.pop()
        stack.append(i)
    return ans

if __name__ == '__main__':
    input = [73, 74, 75, 71, 69, 72, 76, 73]
    t1 = time.time()
    output = dailyTemperatures(input)
    t2 = time.time()
    print(output)
    print ('timeout:', t2-t1)
