set1 = set(map(int,input("Enter the set1:").split(",")))
set2 = set(map(int,input("Enter the set2:").split(",")))
set1 = set1.intersection(set2)
print(set1)