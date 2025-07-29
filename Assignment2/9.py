L = list(eval(input("Enter the list:")))
n = int(input("Enter the value which you want to replace:"))
ele = int(input("Enter the element:"))
for i in L:
    if(L[i]==n):
        L[i]=ele
        break
print(L)