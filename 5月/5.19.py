# source : https://leetcode.cn/problems/integer-to-roman/ 把规则制定好，hash表
class Solution:
    def intToRoman(self, num: int) -> str:
        s = str(num)
        length = len(s)
        d = {1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX",10:"X"}
        res = ""
        while length > 0:
            base = pow(10, length-1)
            t = int(s[0]) * base
            new = ""
            if t == 0:
                break
            if t == base:
                if base == 10:
                    new += "X"
                elif base == 100:
                    new += "C"
                elif base == 1000:
                    new += "M"
                else:
                    new += "I"
            else:
                if base == 10:
                    for i in d[t//10]:
                        if i == "I":
                            new += "X"
                        elif i == "V":
                            new += "L"
                        else:
                            new += "C"
                elif base == 100:
                    for i in d[t//100]:
                        if i == "I":
                            new += "C"
                        elif i == "V":
                            new += "D"
                        else:
                            new += "M"
                elif base == 1000:
                    for i in d[t//1000]:
                        if i == "I":
                            new += "M"
                else:
                    new = d[t]
            num = num - t
            s = str(num)
            res += new
            length = len(s)
        return res


S = Solution()
print(S.intToRoman(58))