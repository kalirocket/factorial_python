def factorial(num):
    if num == 0:
        return 1
    elif num < 0:
        return "Factorial of a negative number is undefined"
    else:
        fac = 1
        for po_int in range(num,0,-1):
            fac = fac * po_int
        return fac

