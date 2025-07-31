set1 = set(map(int,input("Enter the set1:").split(",")))
list  = list(map(int,input("Enter the set2:").split(",")))
set1 = set1.add(set(list))
print(set1)
