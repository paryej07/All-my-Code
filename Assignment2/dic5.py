dic = [{"A":2},{"B":3},{"C":2}]
dic2 = set(val for dict in dic for val in dict.values())
print(dic2)
