def func(num,power):
    if power==0:
        return 1
    else:
        return num * (func(num,power-1))

num=int(input("Enter num: "))
power=int(input("Enter power: "))
print(func(num,power))

