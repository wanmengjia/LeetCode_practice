# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 示例 2:
#
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 说明:
#
# 所有输入只包含小写字母 a-z 
#
class Solution:

    def longestCommonPrefix(self, strs):
        r = [len(set(c))==1 for c in zip(strs)]+[0]
        return  strs[0][:r.index(0)] if strs else " "

    def longestCommonPrefix2(self,strs):
        if strs == []:
            return ""
        # 找到最短字符串
        minstr = min(strs, key=len)
        for i in range(len(strs)):
            #循环最短字符串是否包含
            while strs[i].find(minstr) != 0:
                #不包含减少字符长度
                minstr = minstr[0:len(minstr) - 1]
        return minstr

    def longestCommonPrefix3(self,strs):
        if strs == []:
            return ""
        #以第一个字符串为基准
        CommonPrefix = strs[0]
        #逐个循环比较
        for i in range(1,len(strs)):
            #找到两个字符中最长公共前缀
            CommonPrefix = self.commonprefix(CommonPrefix,strs[i])
        return CommonPrefix

    def commonprefix(self,str1,str2):
        for j in range(len(min(str1, str2))):
            if str1[j] != str2[j]:
                str1= str1[0:j]
                break
        str1 = min(str1, str2)
        return str1




if __name__ == "__main__":
    strs =["flower","flow","flight","flow1"]
    # print(Solution().longestCommonPrefix(strs))
    print(Solution().longestCommonPrefix3(strs))