#przykład 1
n=100
def policz(a,b,c=1):
    global n
    n = (a+b)*c + n
    return n

print(policz(4,7,3))
print(policz(4,7))
print(n)


#przykład 2
num = [67,8.9,-1,0,34,55,100,-99,35,68,98,2,8,0,9]
kr = [(9,4),(9,6),(11,45),(2,101)]

parzyste = list(filter(lambda x:x%2==0,num))
print(parzyste)

cube = list(map(lambda x:x**3,num))
print(cube)

def multifive(n):
    return n*5

five = list(map(multifive,num))
print(five)

def multifiveplus(n):
    return n[0]*5+n[1]

dwa = list(map(multifiveplus,kr))
print(dwa)
