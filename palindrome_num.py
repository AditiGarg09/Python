def check_palindrome(num):
    temp=num
    rem=0
    rev=0
    
    while num>0:
        rem=num%10
        rev=rev*10+rem
        num=num//10

    if temp==rev :
        return "Yes! Number is a Palindrome"
    else:
        return "No! Number is not a Palindrome"
        
num=int(input("Enter num: "))
print(check_palindrome(num))
