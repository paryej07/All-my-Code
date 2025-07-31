set1 = set(map(int,input("Enter the set1:").split(",")))
set2 = set(map(int,input("Enter the items to be removed :").split(",")))
set1 = set1-set2
print(set1)
