import math
start=int(input("Enter a starting range in 4 digits: "))
end=int(input("Enter a ending range in 4 digits: "))
perfect=[]
for i in range(start,end+1):
    num=i
    flag=0
    while num>0:
        digit=num%10
        if digit not in[0,2,4,6,8]:
            flag = 1
            break
        num=int(num//10)
    if flag == 0 and math.isqrt(i) ** 2 == i:
        perfect.append(i)
print("The list of perfect square numbers are:",perfect)