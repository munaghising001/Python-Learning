# qn 4 Accept name and age from the user.Check if the user is a valid voter or not

name = input("enter your Name ->")
age = int(input("enter your age ->"))

if age >= 18:
    print(f" Hell0 {name} you are a Valid voter")
else:
    print(f" Hello {name} you are an invalid voter")
