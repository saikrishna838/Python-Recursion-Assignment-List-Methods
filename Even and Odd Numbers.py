nums = input().split(" ")
even = []
odd = []

for number in nums:
    if int(number) % 2 == 0:
        even.append(int(number))
    else:
        odd.append(int(number))

even.sort()
odd.sort()

print(even)
print(odd)
        