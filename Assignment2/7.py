L = list(map(eval,input("Enter the list:").split(",")))
n = int(input("Enter the value after which you want to add:"))
ele = int(input("Enter the element:"))
for i in L:
    if(L[i]==n):
        L.insert(L[i],ele)
        break
print(L)