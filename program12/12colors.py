n=int(input("enter the number of colors:"))
color_list=[]
for i in range(n):
   color=input("enter the color:")
   color_list.append(color)
print(color_list)
print("the first color is:",color_list[0])
print("the last color is:",color_list[-1])