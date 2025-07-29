L = list(eval(input("Enter the list:")))
n = int(input("Enter the value after which you want to add:"))
ele = int(input("Enter the element:"))
for i in L:
    if(L[i]==n):
        c=i
        break
L.insert(L[c],ele)
print(L)