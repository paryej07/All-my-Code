L = list(map(int, input("Enter the list:").split(",")))
ele = int(input("Enter to remove : "))
while ele in L:
    L.remove(ele)
print(L)
