if 10<2:
    pass
else:
    print("Hello")

table = 10
for i in range(1,11):
    if i==5:
        break
    elif i==2:
        continue
    print(table,"X",i,"=",(table*i))