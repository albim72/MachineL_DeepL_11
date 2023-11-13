#przykład 1
n=100
def policz(a,b,c=1):
    global n
    n = (a+b)*c + n
    return n

print(policz(4,7,3))
print(policz(4,7))
print(n)

