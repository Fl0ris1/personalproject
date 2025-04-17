alphabet="abcdefghijklmnopqrstuvwxyz"
def numSort(x):
    sortedList=[]
    for i in range(0,len(x)):
        sortedList.append(min(x))
        x.remove(min(x))
    return sortedList
    
def letSort(x):
    nums=[]
    sortedList=[]
    for pos in range(0,len(x)):
        for i in range(0,len(alphabet)):
            if x[pos]==alphabet[i]:
                nums.append(i)
    nums=numSort(nums)            
    for i in range(0,len(nums)):
        nums[i]=alphabet[nums[i]]
        
    return nums
    
def alphabetNum(x):
    nums=[]
    for pos in range(0,len(x)):
        for letter in range(0,len(alphabet)):
            if x[pos]==alphabet[letter]:
                nums.append(letter+1)
    return nums
    
