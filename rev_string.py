string=input("Enter string: ")

if " " in string:
    s1=string.split(" ")
    list1=[]

    for i in range(0,len(s1)):
        list1.append(s1[i][::-1])
    
    print(" ".join(list1))

else:
    print(string[::-1])
