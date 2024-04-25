m = int(input())
if m <= 2 or m == 12:
    print("Winter");
elif m <= 5:
    print("Spring");
elif m <= 8:
    print("Summer");
elif m <= 11:
    print("Fall");
else:
    print("wrong input");