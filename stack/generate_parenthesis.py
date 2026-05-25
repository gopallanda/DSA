def generateParenthesis(n):
    res=[]
    def backtrack(current,open,close):
        if len(current)==2*n:
            res.append(current)
            return
        if open<n:
            backtrack(current+"(",open+1,close)
        if close<open:
            backtrack(current+")",open,close+1)
    backtrack("",0,0)
    return res
if __name__=="__main__":
    n=int(input("enter the number of pairs of parentheses:"))
    result=generateParenthesis(n)
    print("All combinations of well-formed parentheses are:",result)