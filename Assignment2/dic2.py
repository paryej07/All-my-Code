dict1 = dict(A=1,B=2,C=3)
dict2 = dict(D=4,E=5,F=6)
dict3 = { }
for i in (dict1,dict2):
    dict3.update(i) 
print(dict3)