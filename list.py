'''
Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
Question taken from https://www.w3resource.com/python-exercises/list/#EDITOR

'''

num=int(input("Enter number of elements you want to enter in a list: "))
list1=[]

print("Now enter",num,"elements")
for i in range(0,num):
    ele=(input())
    list1.append(ele)

count=0

for i in range(0,num):
    ele=list1[i]
    rev=ele[::-1]
    if list1[i]==rev:
        count+=1
      
print(count)
