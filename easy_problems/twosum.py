# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
#
# 示例:
#
# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]

class Solution:
    def twosum(self,nums,target):
       d = {target-n : i for i,n in enumerate(nums)}
       print(d)
       return [[i,d[n]] for i, n in enumerate(nums) if n in d and d[n] >i]

    def twosum1(self,nums,target):
        B= {target-i:index for index,i in enumerate(nums)}
        A= {a:index for index,a in enumerate(nums)}
        listindex =[]
        for b in B:
            if b in A and B[b]<A[b]:
                listindex.append([B[b],A[b]])
        return listindex

    def twosum2(self,nums,target):
        A= {a:index for index,a in enumerate(nums)}
        print(A)
        listindex =[]
        for i in range(len(nums)):
            b = target - nums[i]
            if b in A and A[b]>i:
                listindex.append([i,A[b]])
        return listindex


if __name__ == "__main__":
    # nums = [2,3,5,6,8,9,-1,10,11,12,13,-2]
    nums=[2,3,4,5,6]
    target = 8
    result =Solution().twosum(nums=nums,target=target)
    print(result)
    print(Solution().twosum1(nums=nums,target=target))
    print(Solution().twosum2(nums=nums,target=target))


