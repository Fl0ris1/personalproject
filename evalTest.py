inp=input()
list1=[]

list1=inp.split()
for i in range(1,len(list1)):
    list1[0]+=list1[i]
    
print(round(eval(list1[0]),13))
