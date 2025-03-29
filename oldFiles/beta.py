import os
os.system('cls')
tokens=[]
var=[]
added_var=""
var_num=0
instructions=[]
math_tokens=["+","-","*","/"]
print_tokens=["SayStr","SayInt","Say"]
var_tokens=["VarAdd","VarSay","VarDel","Var"]
console_commands=["cc","clear","end"]
all_tokens=math_tokens+print_tokens+var_tokens+console_commands

"""class Vars:
    def __init__(self):"""
while True:
    tokens=[]
    inp=input("LANGUAGE >")
    tokens=inp.split()
    print(tokens)
    
    #if len(tokens)>1:
    if tokens[0] in all_tokens or tokens[1] in all_tokens:
    #check if tokens used for math
        if tokens[1] in math_tokens:

            if tokens[1]=="+":
                x=int(tokens[0])+int(tokens[2])

            elif tokens[1]=="-":
                x=int(tokens[0])-int(tokens[2])

            elif tokens[1]=="*":
                x=int(tokens[0])*int(tokens[2])

            elif tokens[1]=="/":
                x=int(tokens[0])/int(tokens[2])

    #checks if tokens used for saying
        elif tokens[0]=="Say":

            if tokens[1]=="Str":
                for i in range(2,len(tokens)):
                    print(tokens[i]," ",end="")
                print("")

            elif tokens[1]=="Int":
                for i in range(3,len(tokens)):
                    tokens[2]+=str(tokens[i])
                x=eval(tokens[2])
        
                print(x)

            elif tokens[1]=="Var":
                if tokens[2]=="All":
                    print(var)

                elif tokens[2].isdigit():
                    if int(tokens[2])>len(var)-1:
                        print("LIST INDEX OUT OF RANGE")

                    else:
                        print(var[int(tokens[2])])

    #used for console commands
        elif tokens[0]=="cc" :
            if tokens[1]=="clear":
                os.system('cls')
            if tokens[1]=="end":
                exit()

        elif tokens[0] in var_tokens:
            if tokens[0]=="Var":
                if tokens[1]=="Add":
                    for i in range(2,len(tokens)):
                        if i==len(tokens)-1:
                            added_var=added_var+tokens[i]
                        else:
                            added_var=added_var+tokens[i]+" "

                    var.append(added_var)
                    print(var[var_num])
                    added_var=""
                    var_num+=1

                elif tokens[1]=="Del":
                    if tokens[2].isdigit():
                        if int(tokens[2])>len(var)-1:
                            print("UNABLE TO REMOVE NON-EXISTING OBJECT")
                    
                        else:
                            var.remove(var[int(tokens[2])])
                            var_num-=1
                
                
                    elif tokens[2]=="All":
                        var.clear()
                        var_num=0
            
                
                else:
                    print("SYNTAX ERROR")
            else:
                print("SYNTAX ERROR")
        else:
            print("SYNTAX ERROR")
    
    else:
        print("SYNTAX ERROR")

            
        
