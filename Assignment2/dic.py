import operator
dic = dict(A=5,B=3,C=88,D=2)
dic2 = sorted(dic.items(),key=operator.itemgetter(1))#here the key is for sorted function 
#itemgetter is use fatch item from dictionay
print("Dic:",dic2)