num=int(input("How many elements you wan to enter: "))
list1=[]
list2=[]
for i in range(0,num):
    ele=int(input("Enter element: "))
    list1.append(ele)

for num in list1:
    list2.append(num*num)

print(list1)
print(list2)
