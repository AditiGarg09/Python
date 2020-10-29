name=input("Enter your Name: ")
roll_no=input("Enter your Roll No.: ")
branch=input("Enter your branch: ")
batch=input("Enter your batch: ")

print("Your E-Mail Id:",name+roll_no[-4:]+"."+branch+batch[-2:]+"@chitkara.edu.in")
