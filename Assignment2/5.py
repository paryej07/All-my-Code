L = list(eval(input("Enter the List:")))
L2 = list(eval(input("Enter the List:")))
l = len(L)
if (L2>L):
    l = len(L2)
for i in range(l):
    L[i]+=1
    L2[i]+=1
print("List are:",L,"\n",L2)