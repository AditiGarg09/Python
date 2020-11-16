#Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.

string=input("Enter String: ")
result=string[0]
flag=0
for i in range(1,len(string)):
    for j in result:
        if string[i]!=j:
            flag=1
            
        else:
            flag=0
            break
            
    if flag is 1:
        result+=string[i]
    else:
        result+='$'

print(result)
