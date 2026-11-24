strings="ababcddabc"
hold=[]
hold_2={}
left,right=0,1
first_total,total=0,0
for i in range(len(strings)):
    if strings[i] not in hold:
        hold.append(strings[i])
        total+=1
        right+=1
    else:
        if total>first_total:
            left+=1
            first_total=total
        else:
            left+=1
print(hold_2)
print(first_total)

