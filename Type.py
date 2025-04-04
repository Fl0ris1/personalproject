def TypeCheck(x):#,var
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