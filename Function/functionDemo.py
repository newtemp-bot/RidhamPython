def display():
    print("Hello")
    print("Hyy")
    print("Welcome")

def sumOfTwoValue(a=0,b=0):
    print("A =",a)
    print("B =",b)
    return a+b

def fullname(fname="Temp",lname="Name"):
    print("Your Full Name is = ",fname,lname)

""" 
#You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.

def fullname(fname="Temp",lname="Name",/):
    print("Your Full Name is = ",fname,lname) """

""" 
#To specify that a function can have only keyword arguments, add *, before the arguments:

def fullname(*,fname="Temp",lname="Name"):
    print("Your Full Name is = ",fname,lname) """

def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, d = 8,c = 7)

def fruitsList(*Tuple):
    print("Tuple =",Tuple)

def nameList(list):
    print("List =",list)

def car(**karg):
    print(karg)


fruitsList("Apple","Banana","Mango")


display()
print("Code Start")
print("Code")
print("Code")
print("Code")
print("Code")
print("Code End")
display()
print("Code Start")
print("Code")
print("Code")
print("Code End")
fullname("Ashok","Rathod")
fullname(lname="Rathod",fname="Ashok")
car(name="BMW",id=1254,model="S3",year=2020)
fullname()

listdata = ["Ashok","pooja","Rahul"]
nameList(listdata)

value = sumOfTwoValue(50,60)

print(value)