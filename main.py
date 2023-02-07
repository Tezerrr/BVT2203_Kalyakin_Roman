def lol():
    a,b,c = map(int, input().split(" "))
    d = b**2-4*a*c
    return (-b+d**0.5)/(2*a), (-b-d**0.5)/(2*a)
print(lol())