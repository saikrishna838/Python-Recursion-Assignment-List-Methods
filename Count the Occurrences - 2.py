nums = input().split(" ")
new_list = []
length = len(nums)

for i in range(length):
    occurs = nums.count(nums[i])
    if int(occurs) % 2 != 0:
        new_list += [nums[i]]
new_list = list(map(int, new_list))  
result = list(set(new_list))
result.sort()
print(result)