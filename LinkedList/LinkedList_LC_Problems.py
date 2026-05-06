class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def mergeLists(l1,l2):
    dummy=ListNode()
    current=dummy
    while l1 and l2:
        if l1.val<l2.val:
            current.next=l1
            l1=l1.next
        else:
            current.next=l2
            l2=l2.next
        current=current.next
    if l1:
        current.next=l1
    if l2:
        current.next=l2
    return dummy.next

def palindromeList(head):
    if not head or head.next:
        return False
    slow=fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    uc=pr=None
    while slow:
        uc=slow.next
        slow.next=pr 
        pr=slow 
        slow=uc 
    slow=pr
    left,right=head,slow
    while right:
        if left.val!=right.val:
            return False
        left=left.next
        right=right.next
    return True

def reverseList(head):
    uc=pr=None
    while head:
        uc=head.next 
        head.next=pr 
        pr=head
        head=uc
    head=pr 
    return head 