list1=["black",1,2.6,3,5,7.8,9.4,"red","blue"]
list2=[]
list3=[]
list4=[]
for i in list1:
    type_var=type(i)
    
    if type_var==str:
        list2.append(i)
    elif type_var==int:
        list3.append(i)
    elif type_var==float:
        list4.append(i)
print("Original List:",list1)
print("String List:",list2)
print("Integer List:",list3)
print("Float List:",list4)
