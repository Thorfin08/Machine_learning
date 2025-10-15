
test ={
 'input': 
 {
     'cards':[13,11,10,7,4,3,1,0],
     'query': 7
 },
 'output': 3
}
tests=[]
tests.append(test)
tests.append({
 'input':   
 {
     'cards':[13,11,10,7,4,3,1,0],
     'query': 1
 },
 'output': 6
})
tests.append({
 'input':{
     'cards':[4,2,1,-1],
     'query': 4
    },
 'output':0
})
tests.append({
    'input':{
        'cards':[6],
        'query':7
    },
    'output': -1

})

print(tests)

def locate_card(cards,query):

    position=0
    while True:
        if cards[position]==query:
            return position
        position+=1
        if position==len(cards):
            return -1

result=locate_card(test['input']['cards'], test['input']['query'])
if result == test['output']:
    print("Test passed")
