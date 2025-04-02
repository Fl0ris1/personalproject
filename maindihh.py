array=[0]
pos=0
stack=[]
num_check=[]
isFloat=False
isInt=False
isStr=False
#constant
stack_pointer=0
digits="1234568790." #ADD DIFFERENTIATOR BETWEEN STR INT AND FLOAT FOR INPUT INSTRUCTION
inp=input()
for i in range(0,len(inp)):
    if inp[i]==" ":
        i+=1
        
    elif inp[i]==".":
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
                   
        
    elif inp[i]==";":
        stack.append(array[pos])
        array[pos]=0
        
    elif inp[i]==":":
        array[pos]=stack[stack_pointer]
        stack.remove(stack[stack_pointer])
        
    elif inp[i]=="#":
        array[pos]=array[pos]+array[pos+1]
