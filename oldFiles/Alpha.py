list1=[]
reg_nr=0

while True:
    if reg_nr>len(list1)-1:
        reg_nr=0
    
    elif reg_nr<0:
        reg_nr=len(list1)-1
    
    inp=input()
    
    if inp=="<>":
        inp1=int(input())
        reg_nr=inp1
    
    elif inp==">":
        reg_nr=reg_nr+1
        
        
    elif inp=="<":
        reg_nr=reg_nr-1
    
    elif inp=="++":
        inp1=int(input())
        list1.append(inp1)
    
    elif inp=="--":
        y=list1[reg_nr]
        list1.remove(y)
        #reg_nr=reg_nr-1
        print(len(list1))
    
    elif inp=="/":
        print(list1)
        
    elif inp=="dbg":
        print(reg_nr)
        print(len(list1))
