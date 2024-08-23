def some(n):
    return n *(n+1)/2
def arraysome(a):
    some = 0
    for i in a:
        some = some + i
    return (some)
a = [1,3,5,5,7]
arraysome(a)

def someone(n):
    if (n<= 0):
        return 
    return n + someone(n-1)
