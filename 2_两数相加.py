"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
主要注意以下几点：
1）终止条件：某一个遍历结束时，另外一个后半段要直接拷贝or赋值，最后的进位也要是0才终止
2）两数相加可能存在进位，加到下一次求和上
3）初始化listnode时，可能存在多余节点，于是返回next节点
"""
# Definition for singly-linked list.
#class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        rep = result
        p = l1
        q = l2
        carry = 0
        while(p or q or carry != 0):
            valp = p.val if p else 0
            valq = q.val if q else 0
            allsum = valp + valq + carry  #累加进位
            rep.next = ListNode(allsum % 10)
            rep = rep.next
            carry = allsum // 10
            p = p.next if p else None
            q = q.next if q else None
        return result.next #初始化根节点没用，否则结果个位会多个0
