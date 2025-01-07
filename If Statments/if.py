age = int(input("Enter your age = "))

""" 
if age>=18:
    print("You are eligable for licences")
else:
    print("You are not eligable for lincence")

if age>=16:
    print("you are eligable for learning licences")
else:
    print("You are not eligable for lincence") 
"""

if age>=18:
    print("You are eligable for licences")
    evalu = input("Enter value y or n = ")
    if evalu=="y":
        print("Yes you have enter")
    if evalu=="n":
        print("no you have not enter")
elif age>=16:
    print("you are eligable for learning licences")
else:
    print("You are not eligable for lincence") 