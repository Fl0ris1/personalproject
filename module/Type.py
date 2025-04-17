def check(x):#,var
    isStr=False
    isInt=False
    isFloat=False
    dotCount=x.count(".")

    if x.isdigit():
        isInt=True
    else:
        for i in range(0,len(x)):
            if x[i].isdigit() and "." in x and dotCount==1 and x[len(x)-1]!="." and x[0]!=".":
                isFloat=True
            else:
               isStr=True
            
    if isInt==True:
        y="INT"
    elif isFloat==True:
        y="FLOAT"
    elif isStr==True:
        y="STRING"

    return y
    
def isNum(x,z):#FIX TS (LK STRING NUMBERS AND FLOATS)
    isOdd=False
    isEven=False
    if z==True:
        if type(x)!=str:
            if x%2==0:
                isEven=True
            else:
                isOdd=True
    elif z==False:
        if type(x)!=str and type(x)!=float:
            if x%2==0:
                isEven=True
            else:
                isOdd=True
    
    if isOdd==True:
        y="ODD"
    elif isEven==True:
        y="EVEN"
        
    return y
        
