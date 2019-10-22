# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
# 有效字符串需满足：
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。
#
# 示例 1:
#
# 输入: "()"
# 输出: true
# 示例 2:
#
# 输入: "()[]{}"
# 输出: true
# 示例 3:
#
# 输入: "(]"
# 输出: false
# 示例 4:
#
# 输入: "([)]"
# 输出: false
# 示例 5:
#
# 输入: "{[]}"
# 输出: true


class solution():

    def isvalid(self,str):
        list = "(){}[]"
        dict = {"(":")","{":"}","[":"]"}
        if len(str)%2 !=0 or str == " " or str=="":
            return False
        else :
            listdict =[]
            for i in str:
                if list.find(i) == -1:
                    return False
                listdict.append(i)
                if len(listdict)>=2:
                    if listdict[-2] not in dict:
                        return False
                    elif dict[listdict[-2]] == i:
                        listdict.pop()
                        listdict.pop()
            if listdict ==[]:
                return True
            else:
                print(listdict)
                return False

    def isvalid2(self, str):
        list = "(){}[]"
        dict = {"(": ")", "{": "}", "[": "]"}
        if len(str) % 2 != 0 or str == " ":
            return False
        else:
            listdict = []
            for i in str:
                if list.find(i) == -1:
                    return False
                if i in dict:
                    listdict.append(i)
                elif listdict != []:
                    if dict[listdict[-1]] == i:
                            listdict.pop()
                    else:
                        return False
                else:
                    return False
            if listdict == []:
                return True



if __name__ == "__main__":
    str ="(}[][]"
    print(solution().isvalid2(str))

