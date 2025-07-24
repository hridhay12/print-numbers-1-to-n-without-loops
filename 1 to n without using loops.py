def printTillN(n):
    if n > 1:
        printTillN(n - 1)
    print(n, end=' ')

d=int(input("Enter a number: "))
printTillN(d)
