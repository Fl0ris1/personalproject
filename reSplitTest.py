import re
"""list1=["a","b"]
list2=["c","d"]
list3=[list1+list2]
print(list3)
inp=input()
if inp[0] in list3:
    print("hi")
else:
    print("no")"""

inp=input()
list1=[]
list1=re.split(r'\s', inp)
for i in range(1,len(list1)):
    list1[0]+=list1[i]
print(list1[0])
