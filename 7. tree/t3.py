def f1():
    a1 = 1
    def f2():
        # nonlocal a1
        # a1=3
        # a1.append(2)
        print(a1)
    print(a1)
    f2()
    print(a1)

f1()