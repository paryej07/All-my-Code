L = list(eval(input("Enter the list:")))
B = []
for i in range(len(L)):
    B.append(L[i]*L[i])
print("List:",B)