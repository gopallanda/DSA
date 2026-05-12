def reverseInKGroup(head,k):
    if head is None or head.next is None or k == 1:
        return head

    def reverse(current,k):
        uc=pr=None
        while k>0:
            uc=current.next
            current.next=pr
            pr=current
            current=uc
            k-=1 
        return pr, current
    temp=head
    length=0
    while temp:
        length+=1
        temp=temp.next
    n=length//k
    dummy=ListNode(0)
    dummy.next=head
    pre=dummy
    curr=head
    for i in range(n):
        new_head,nxt=reverse(curr,k)
        pre.next=new_head
        curr.next=nxt
        pre=curr
        curr=nxt
    return dummy.next
        