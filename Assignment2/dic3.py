dic = dict(A=5,B=3,C=88,D=2)
dic2 = dict(E=5,F=3,G=88,H=2)
dic3 = dict()
for i in (dic,dic2):
    dic3.update(i)
print(dic3)