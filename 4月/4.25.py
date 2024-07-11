# source: https://leetcode.cn/problems/total-distance-traveled/description/

mainTank = int(input("主油箱"))
additionalTank = int(input("副油箱"))
distance = 0
while mainTank >= 5 and additionalTank > 0:
    mainTank -= 5
    distance += 50
    additionalTank -= 1
    mainTank += 1
distance += mainTank*10
print(distance)

