test = {
    'input': {
        'cards': [13, 11, 10, 9, 7, 6, 4, 4, 4, 4, 3],
        'query': 4
    },
    'output': 6
}

print("Test input:", test['input'])

def locate_card(cards, query, mid):
    if cards[mid] == query:
        if mid - 1 >= 0 and cards[mid - 1] == query:
            return 'left'
        else:
            return 'found'
    elif cards[mid] > query:    
        return 'right'
    else: 
        return 'left'

print("xyaaa")

def binary_search(cards, query):
    lo = 0
    hi = len(cards) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        print('lo', lo, 'hi', hi, 'mid', mid, 'cards[mid]', cards[mid])
        result = locate_card(cards, query, mid)
        if result == 'right':
            lo = mid + 1
        elif result == 'left':
            hi = mid - 1
        elif result == 'found':
            return mid
    return -1 

final_result = binary_search(test['input']['cards'], test['input']['query'])

if final_result == test['output']:
    print('Test passed', final_result)
else:
    print('Test failed. Got', final_result)

