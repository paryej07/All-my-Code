L = list(map(eval,input("Enter the list:").split(",")))
for i in L:
    L.remove('')
print(L)