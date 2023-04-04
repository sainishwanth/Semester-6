Str = input()
n = int(input())
lst = list(Str)

print(len(lst))

if n <= len(Str):
    for i in range(len(lst)):
        if n + i > len(lst):
            print(f"idk: {n+i}")
            lst[i] = lst[(n+i)-len(lst)]
            print((n+i)-len(lst))
        else:
            print(f"else: {i}")
            if (n+i) == len(lst):
                lst[i] = lst[len(lst)]
            else:
                lst[i] = lst[n+i]
    print(''.join(lst))
else:
    print("Invalid Input")
