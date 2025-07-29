L = tuple(map(int,input("Enter the Elements:").split(",")))
R = list(L)
L = tuple(R[::-1])
print(L)