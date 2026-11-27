strings=[100, 4, 200, 1, 3, 2]
strings.sort()
hold={}
first_loss=1
get_different=1
for i in range(len(strings)-1):
    if  strings[i+1]-strings[i]==first_loss:
        if get_different not in hold.keys():
            hold[get_different]=[]
        else:
            hold[get_different].append(strings[i])
    else:
        first_loss=strings[i+1]-strings[i]
        get_different+=1
        
print(hold)

    
    
    
    