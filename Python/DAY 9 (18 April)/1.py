def outer():
    n=10
    def inner():
        nonlocal n
        print("Inner Function")
        print(n)
        n=n+1
        print(n)
    inner()
outer()

