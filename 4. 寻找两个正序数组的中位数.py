"""
给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数。

进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

#下面方法是时间和空间复杂度都是o(m+n)
#可以进一步优化一下是，如果两个长度都已知，则维护两个下标，或者指针，一步步内部移动到指定下标即可，起码不用浪费存储空间了（待优化）
#复杂度有log出现的一般都是二分法，AB长度已知，则找(lenA+lenB)/2即可，将A和B切分，逐渐内层切分即可（待优化）
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = []
        if not nums1:
            nums = nums2
        elif not nums2:
            nums = nums1
        else:
            index1 = 0
            index2 = 0
            while (index1 < len(nums1) or index2 < len(nums2)):
                if index1 < len(nums1) and index2 < len(nums2):
                    if nums1[index1] < nums2[index2]:
                        nums.append(nums1[index1])
                        index1 += 1
                    else:
                        nums.append(nums2[index2])
                        index2 += 1
                elif index1 < len(nums1):
                    nums.append(nums1[index1])
                    index1 += 1
                else:
                    nums.append(nums2[index2])
                    index2 += 1
        length = len(nums)
        result = (nums[length//2-1] + nums[length//2]) / 2 if length % 2 == 0 else nums[length//2]
        return result
