w=input("enter a word:")
ord=[ord (x) for x in w]
print("the ordinal value is:",ord)

num_list = [-1,-2,-3,0,4,5,6,7,8,9]
print(num_list)
newlist=[x for x in num_list if x>0]
print("The positive numbers are:",newlist)

n=int(input("Enter the number of elements:"))
num_list=[]
for i in range(n):
 a=int(input("Enter the numbers:"))
 num_list.append(a)
print("Entered list:",num_list)
sqr_lst=[x**2 for x in num_list]
print("Squared list:",sqr_lst)

word=input("Enter a word:")
vowels=[x for x in word.lower()if x in['a','e','i','o','u']]
print("The vowels are:",vowels)
