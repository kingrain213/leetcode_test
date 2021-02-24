"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

 

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import numbers

#暴力检索方法，两层循环，时间复杂度O(N2)
def violence_search(nums: list, target:numbers.Number) ->list:
    for index, val in enumerate(nums):
        for j in (range(index+1, len(nums))):
            if val + nums[j] == target:
                return [index, j]
    return None


#hash_map映射方法，采用一层循环便达到效果
#dict的key可以是int、str、但不能是list
def hash_search(nums:list, target:numbers.Number) -> list:
    detais = dict()
    for index, val in enumerate(nums):
        if target - val in detais.keys():
            return [detais[target-val], index]
        detais[val] = index
    return None

if __name__ == '__main__':
    nums = [1,2,3,4]
    target = 5
    result = violence_search(nums, target)
    print(result)
