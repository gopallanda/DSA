'''
n people from 1 to n are standing in the queue at a movie ticket counter. It is a weird counter, as it distributes tickets to the first k people and then the last k people and again first k people and so on, once a person gets a ticket moves out of the queue. The task is to find the last person to get the ticket.

Examples:

Input: n = 9, k = 3
Output: 6
Explanation:
Starting queue will like [1, 2, 3, 4, 5, 6, 7, 8, 9]. After the first distribution queue will look like [4, 5, 6, 7, 8, 9].
And after the second distribution queue will look like [4, 5, 6]. The last person to get the ticket will be 6.
'''
from collections import deque
def ticketCounter(n,k):
    q=deque([i+1 for i in range (n)])
    counter=k 
    for i in range(n//k):
        if counter<=k and counter>0:
            for i in range(k):
                last_poped=q.popleft()
                counter-=1
        elif counter==0:
            for i in range(k):
                last_poped=q.pop()
                counter-=1
        elif counter<0:
            for i in range(k):
                last_poped=q.popleft()
                counter+=1
    if counter==0:
        for i in range(len(q)):
            last_poped=q.pop()
    else:
        for i in range(len(q)):
            last_poped=q.popleft()
    return last_poped
    
    
#the time complexity of above solution is 0(n) and space complexity also 0(n) as we are storing the elements, we can do without using deque and any pop operations which reduces the time complexity to 0(n/k) 

'''
Complexity
Time: O(n/k) (each iteration removes k people)
Space: O(1)
This is much better than simulating the queue with a deque (O(n) space).
'''

def ticketCounterOp(n,k):
    left=1
    right=n 
    remaining=n
    front= True  
    while remaining>k:
        if front:
            left+=k
        else: 
            right-=k 
        remaining-=k 
        front= not front 
    if front:
        return right 
    else:
        return left 
# even more easier code but TC is 0(n)

def counter(n,k):
  q=deque([i+1 for i in range(n)])
  print(q)
  if n==1:
        return q[0]
  while True:
    for _ in range(k):
        q.popleft()
        if len(q)==1:
            return q[0]
    for _ in range(k):
        q.pop()
        if len(q)==1:
            return q[0]

if __name__=="__main__":
    n=int(input("enter n:"))
    k=int(input("enter k:"))
    res=ticketCounter(n,k)
    opres=ticketCounterOp(n,k)
    easyres=counter(n,k)
    print(res)
    print(opres)
    print(easyres)