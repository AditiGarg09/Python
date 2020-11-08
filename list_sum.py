num=int(input("Enter number of elements you want to enter in List: "))
lst1=[]

print("Enter",num,"Elements now")
for i in range(0,num):
    ele=int(input())
    lst1.append(ele)

sum=0
for i in lst1:
    sum+=i
print("Sum of Elements:",sum)
