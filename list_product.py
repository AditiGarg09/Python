num=int(input("Enter number of elements you want to enter in a list: "))
list1=[]

print("Now enter",num,"elements")
for i in range(0,num):
    ele=int(input())
    list1.append(ele)

product=1
for i in list1:
    product *= i
print("Product of elements:",product)
