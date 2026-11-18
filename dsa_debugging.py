list_1=[1,2,3,4,5,4,3,2,3,2,3,2,3,4,5]
hold={}
for i in list_1:
    if i in hold.keys():
        hold[i]=hold[i]+1  
    else:
        hold[i]=1
for i in hold:
    if hold[i]<1:
        print(f"{i} appears 1 times")
        break