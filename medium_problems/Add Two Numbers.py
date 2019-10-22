# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 示例：
#
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self,l1,l2):
        num3 = self.getnum(l1)+self.getnum(l2)
        l3 = list(reversed(str(num3)))
        return l3

    def getnum(self,list):
        num = 0
        if list == []:
            num = 0
        else:
            for i in reversed(list):
                num = num*10 + int(i)
        return num

    def addTwoNumbers1(self,l1,l2):
        lens1 = len(l1)
        lens2 = len(l2)
        

if __name__ == "__main__":
    l1=[1,7,3]
    l2=[2,3,7]
    result = Solution().addTwoNumbers(l1,l2)
    print(result)
    # print(Solution().addTwoNumbers1(l1,l2))



