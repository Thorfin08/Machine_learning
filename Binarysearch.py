test={
    'input':{
        'cards':[9,7,6,4,3,2,1],
        'quary':1
    },
    'output':6

}

def binarysearch(cards, quary):
    lo = 0
    hi = len(cards) - 1

    while lo<=hi:
        mid = (lo+hi)//2
        print("lo:", lo, "hi:", hi, "mid:", mid, "cards[mid]:", cards[mid], "quary:", quary)
        if cards[mid]==quary:
            return mid
        elif cards[mid]<quary:
            hi=mid-1
        elif cards[mid]>quary:
            lo=mid+1

    
    return -1 
result=binarysearch(test['input']['cards'],test['input']['quary'])       
if result == test['output']:
    print("Test passed with an output of:", result)