n=int(input("enter the number of elements in the list: "))
num_list=[]
for i in range(n):
    x=int(input("enter the elements: "))
    if x<100:
        num_list.append(x)
    else:
        num_list.append('over')
print(num_list)