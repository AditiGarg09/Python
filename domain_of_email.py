email=input("Enter E-Mail: ")
if '@' in email:
    domain=email.split('@')[1]
    print("Domain of E-Mail is",domain)
else:
    print("Not a valid E-Mail")
