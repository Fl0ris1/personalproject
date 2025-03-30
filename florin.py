from clear_screen import clear
import re
clear()
tokens=[]
var=[]
added_var=""
var_num=0
stack=""
instructions=[]
intsort=[]
strsort=[]
intused=False
strused=False
temp_string=""
math_tokens=["+","-","*","/"]
print_tokens=["SayStr","SayInt","Say"]
var_tokens=["VarAdd","VarSay","VarDel","Var"]
console_commands=["cc","clear","end"]
all_tokens=math_tokens+print_tokens+var_tokens+console_commands

while True:
    tokens=[]
    stack=""
    intsort=[]
    strsort=[]
    intused=False
    strused=False
    inp=input("LANGUAGE >")
    tokens=inp.split()
    print(tokens)
    for i in range(0,len(tokens)):
            stack+=tokens[i]
    
    #if len(tokens)>1:
    if tokens[0] in all_tokens or stack[0].isdigit():
    #check if tokens used for math
        if stack[0].isdigit():
        #if tokens[0].isdigit(): #in math_tokens:
            for i in range(1,len(tokens)):
                tokens[0]+=tokens[i]
            print(round(eval(tokens[0]),13))

    #checks if tokens used for saying
        elif tokens[0]=="Say":
            tokens=re.split(r"Say |;; | ;; | ;;|;;",inp)
            for i in range(1,len(tokens)):
                temp_string=tokens[i]

                if temp_string[0]=="I" and temp_string[1]=="n" and temp_string[2]=="t" :
                    re.split(r"Int|Int ",temp_string)
                    temp_string=temp_string.replace("Int ","")
                    temp_string=temp_string.strip()
                    intsort.append(temp_string)
                    intused=True

                if temp_string[0]=="S" and temp_string[1]=="t" and temp_string[2]=="r" :
                    re.split(r"Str|Str ",temp_string)
                    temp_string=temp_string.replace("Str ","")
                    temp_string=temp_string.strip()
                    strsort.append(temp_string)
                    strused=True

            if intused==True:
                for i in range(0,len(intsort)):
                    print(round(eval(intsort[i]),13))
            if strused==True:
                for i in range(0,len(strsort)):
                    print(strsort[i],end=" ")
            print("")

            if tokens[1]=="Var": #add variable to say function
                if tokens[2]=="All":
                    for i in range(0,len(var)):
                        print(f"Variable number {i}: (",var[i],end=") ")
                    print("")

                elif tokens[2].isdigit():
                    if int(tokens[2])>len(var)-1:
                        print("LIST INDEX OUT OF RANGE")

                    else:
                        print(var[int(tokens[2])])

    #used for console commands
        elif tokens[0]=="cc" :
            if tokens[1]=="clear":
                clear()
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

            
        
