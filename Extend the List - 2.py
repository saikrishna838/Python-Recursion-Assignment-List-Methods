def extend_list(N):
    all_strings = []

    for _ in range(N):
        line = input().split()
        all_strings.extend(line)
        
    all_strings.sort()
    print(all_strings)

N = int(input())
        
extend_list(N)