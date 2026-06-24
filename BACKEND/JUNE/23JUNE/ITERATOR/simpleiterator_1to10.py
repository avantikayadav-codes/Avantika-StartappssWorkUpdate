a=range(1,11)
it=iter(a)
while True:
    try:
        x=next(it)
        print(x)
    except StopIteration:
        break

