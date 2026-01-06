a = input().split(" ")
b = input().split(" ")

length = len(a) * 2
new_list = []
count1 = 0
count2 = 1

for i in range(length):
    if i % 2 == 0:
        new_list += [a[i - count1]]
        count1 += 1
    else:
         new_list += [b[i - count2]]
         count2 += 1
         
         
print(new_list)
    
        
        



