import os
os.system('cls')
tokens=[]
var=[]
added_var=""
var_num=0
instructions=[]
math_tokens=["+","-","*","/"]
print_tokens=["SayStr","SayInt"]
var_tokens=["VarAdd","VarSay","VarDel"]
console_commands=["cc","clear"]
all_tokens=[math_tokens+print_tokens+var_tokens+console_commands]

"""class Vars:
    def __init__(self):"""
while True:
    tokens=[]
    inp=input("LANGUAGE >")
    tokens=inp.split()
    print(tokens)
    
    if len(tokens)>1:
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
        elif tokens[0] in print_tokens:

            if tokens[0]==print_tokens[0]:
                tokens.remove(tokens[0])
                for i in range(0,len(tokens)):
                    print(tokens[i]," ",end="")
                print("")

            elif tokens[0]==print_tokens[1] and tokens[2] in math_tokens:

                if tokens[2]=="+":
                    x=int(tokens[1])+int(tokens[3])


                elif tokens[2]=="-":
                    x=int(tokens[1])-int(tokens[3])
            

                elif tokens[2]=="*":
                    x=int(tokens[1])*int(tokens[3])
            

                elif tokens[2]=="/":
                    x=int(tokens[1])/int(tokens[3])
        
                print(x)

    #used for console commands
        elif tokens[0]=="cc" :
            if tokens[1]=="clear":
                os.system('cls')

        elif tokens[0] in var_tokens:
            if tokens[0]=="VarAdd":

                for i in range(1,len(tokens)):
                    if i==len(tokens)-1:
                        added_var=added_var+tokens[i]
                    else:
                        added_var=added_var+tokens[i]+" "

                var.append(added_var)
                print(var[var_num])
                added_var=""
                var_num+=1

            elif tokens[0]=="VarSay":
                if tokens[1]=="All":
                    print(var)

                else:
                    if int(tokens[1])>len(var)-1:
                        print("LIST INDEX OUT OF RANGE")

                    else:
                        print(var[int(tokens[1])])

            elif tokens[0]=="VarDel":
                if tokens[1].isdigit():
                    if int(tokens[1])>len(var)-1:
                        print("UNABLE TO REMOVE NON-EXISTING OBJECT")
                    
                    else:
                        var.remove(var[int(tokens[1])])
                        var_num-=1
                
                
                elif tokens[1]=="All":
                    var.clear()
                    var_num=0
            
                
                else:
                    print("SYNTAX ERROR")

        else:
            print("SYNTAX ERROR")
    
    else:
        print("SYNTAX ERROR")

            
        