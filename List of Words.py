s = input().split(" ")
new_list = []

for word in s:
    if word[0] == 'a':
        continue
    else:
       new_list += [word] 
        
print(new_list)