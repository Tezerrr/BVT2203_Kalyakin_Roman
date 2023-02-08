def lol():
    a,b,c = map(int, input().split(" "))
    d = b**2-4*a*c
    if d>0:
        return (-b+d**0.5)/(2*a), (-b-d**0.5)/(2*a)
    if d ==0:
        return (-b)/(2*a)
    if d <0:
        return "Корней нет"
print(lol())