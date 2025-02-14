
myName="john"







def my_function():
    x=29
    return f"{myName} defined variable {x} as a local variable"


print(my_function())
print(myName)

#enclosing scope
def outer ():
    y=47
    def inner():
        nonlocal y

        y+=3
        return y
    inner()
    print(y)
print(outer())