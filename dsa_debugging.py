strings_1="malayalam"
strings_2="malayalams"
output=True
strings_1=set(strings_1)
strings_2=set(strings_2)
for i in strings_1:
    if len(strings_1)==len(strings_2):
        if i not in strings_2:
            output=False
            break
print(output)
