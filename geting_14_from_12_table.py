list1=[]
list2=[]
for i in range(1,11):
    list1.append(12*i)
print(list1)

j=1
for i in list1:
    list2.append(i+(2*j))
    j=j+1
print(list2)
