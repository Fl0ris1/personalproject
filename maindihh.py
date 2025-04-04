import Type
check=Type.TypeCheck
array=[0]
pos=0
stack=[]
num_check=[]
tokens=[]
#constant
stack_pointer=0
inp=input()
inp.replace(" ","")
for i in range(0,len(inp)):
    if inp[i]==".":
        array.append(0)
        pos=len(array)-1
        
    elif inp[i]==",":
        if len(array)>0:
            array.remove(array[pos])
            
    elif inp[i]=="/":
        for i in range(0,len(array)):
            print(array[i],end="")
        
    elif inp[i]==">":
        pos+=1
        if pos>len(array)-1:
            pos=0
             
    elif inp[i]=="<":
        pos-=1
        if pos<0:
            pos=len(array)-1
            
    elif inp[i]=="+":
        array[pos]+=1
        
    elif inp[i]=="-":
        array[pos]-=1
        
    elif inp[i]=="'":
        inp1=input()
        if check(inp1)=="FLOAT":
            array[pos]=float(inp1)
        elif check(inp1)=="INT":
            array[pos]=int(inp1)
        elif check(inp1)=="STRING":
            array[pos]=str(inp1)               
        
    elif inp[i]==";":
        stack.append(array[pos])
        array[pos]=0
        
    elif inp[i]==":":
        array[pos]=stack[stack_pointer]
        stack.remove(stack[stack_pointer])
        
    elif inp[i]=="#":
        array[pos]=array[pos]+array[pos+1]

    elif inp[i]=="*":
        if 
