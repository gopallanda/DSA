def checkIn(a,b,c,d,e):
    a=int(a)
    b=int(b)
    c=int(c)
    d=int(d)
    e=int(e)
    if (a+b)<=d and c<=e :
        return True
    else:
        return False
if __name__=="__main__":
    T=int(input("enter number of test cases:"))
    for i in range(T):
        a,b,c,d,e=tuple(input().split())
        res=checkIn(a,b,c,d,e)
        if res:
            print("Yes")
        else:
            print("No")
    