age=int(input("Enter age: "))
sex=input("Enter sex(M or F): ")
martial_status=input("Enter martial_status(Y or N): ")
if sex == "F" or sex=='f':
    print("Work in urban areas only")
elif sex == "M" or sex=='m':
    if age >=20 and age<=40:
        print("Work anywhere")
    elif age>40 and age<=60:
        print("Work in urban areas only")
    else:
        print("ERROR")
