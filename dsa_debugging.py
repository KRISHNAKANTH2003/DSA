strings=[100, 4, 200, 1, 3, 2]
strings.sort()
sequence=[]
print(strings)
hold={}
total=0
for i in range(len(strings)-1):
    total+=1
    if strings[i]-strings[i+1]==-1:
        if total not in hold.keys():
            hold[total]=[strings[i]]
        else:
            hold[total].append(strings[i])
    else:
        total+=1
print(hold)


