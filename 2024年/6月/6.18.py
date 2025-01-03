# source:https://leetcode.cn/problems/apply-discount-to-prices/


class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        res = ""
        i = 0
        while i<len(sentence):
            if ((i==0 or (i>0 and sentence[i-1]==" ")) and sentence[i]=="$"):
                j = i+1
                while j<len(sentence):
                    if sentence[j]>="0" and sentence[j]<="9":
                        j+=1
                    else:
                        break
                print(i, j,len(sentence))
                if (j==len(sentence) and j!=i+1) or (j < len(sentence) and sentence[j]==" " and j != i+1):
                    num = "{:.2f}".format(int(sentence[i+1:j]) * (1-discount / 100))
                    res += "$"+str(num)
                else:
                    res += sentence[i:j]
                i = j
            else:
                res += sentence[i]
                i += 1
        return res
