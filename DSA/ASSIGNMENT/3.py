set1 =set(map(int,input("Enter the set1:").split(",")))
set2 = set(map(int,input("Enter the set1:").split(",")))
u = set1.union(set2) - set1.intersection(set2)
print(u)