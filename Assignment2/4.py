L = list(eval(input("Enter the List:")))
L2 = list(eval(input("Enter the List:")))
l = len(L)
for i in range(len(L)):
    L.append(L2[i])
print("List are:",L)