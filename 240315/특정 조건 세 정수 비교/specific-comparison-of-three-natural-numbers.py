a = list(map(int, input().split()))
if min(a) == a[0]:
    print(1, end=' ')
else:
    print(0, end=' ')

if len(set(a)) == 1:
    print(1)
else:
    print(0)