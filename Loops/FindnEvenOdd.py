s = int(input("Enter your start nubmer (even and odd) = "))
n = int(input("Enter your end nubmer (even and odd) = "))
listodd = []
lisiteven = []


for i in range(s,n+1):
    if (i%2==0):
        lisiteven.append(i)
    else:
        listodd.append(i)
    
print("Even =",lisiteven)
print("Odd =",listodd)