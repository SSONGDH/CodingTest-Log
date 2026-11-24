a, b, c, d = map(int, input().split())

if(c/2<a):
    if(d/2<b):
        if(c-a>d-b):
            print(d-b)
        else:
            print(c-a)
    else:
        if(c-a>b):
            print(b)
        else:
            print(c-a)
else:
    if(d/2>b):
        if(b>a):
            print(a)
        else:
            print(b)

    else:
        if(a>d-b):
            print(d-b)
        else:
            print(a)
