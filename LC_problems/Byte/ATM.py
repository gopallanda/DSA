def ATM_WithDraw(n,k,cash):
    res=[]
    for i in range(n):
        if cash[i]<=k:
            res.append(1)
            k=k-cash[i]
        else:
            res.append(0)
    return res  
if __name__=="__main__":
    T=int(input("enter number of test cases:"))
    cash=[]
    for i in range(T):
     N=int(input("enter number of persons in the queue:"))
     K=int(input("enter total amount in  ATM:"))
     cash=list(map(int,input().split()))
     op=ATM_WithDraw(N,K,cash)
     print(op)
     
    