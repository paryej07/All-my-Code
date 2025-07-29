A = [[1,2,[1,3,4,[5,6,7]]]]
L = list(eval(input("Enter the list:")))
for j in range(len(L)):
    A.append(L[j])
print(A)