class ListNode():
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
class MergeNodes():
    def mergeNodes(self,lists):
        dummy=ListNode()
        current=dummy
        for head in lists:
            ptr=head
            while ptr:
                current.next=ptr
                ptr=ptr.next 
                current=current.next
        return self.sortLists(dummy.next)
    def sortLists(self,head):
        if not head or not head.next:
            return head 
        prev=None 
        slow=fast=head 
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        prev.next=None
        left=self.sortLists(head)
        right=self.sortLists(slow)
        return self.mergeSort(left,right)
    def mergeSort(self,left,right):
        dummy=ListNode()
        current=dummy
        while left and right:
            if left.val<right.val:
                current.next=left
                left=left.next  
            else:
                current.next=right
                right=right.next
            current=current.next
        if left:
            current.next=left   
        if right:
            current.next=right
        return dummy.next 

def buildLinkedList(arr):
    dummy=ListNode()
    current=dummy
    for val in arr:
        current.next=ListNode(val)
        current=current.next
    return dummy.next
if __name__=="__main__":
    lists = [
        buildLinkedList([1,4,5]),
        buildLinkedList([1,3,4]),
        buildLinkedList([2,6])]
    print("Input linked lists:")
    for l in lists:
        temp=l
        while temp:
            print(temp.val,end=" -> ")
            temp=temp.next
        print("None")
    obj=MergeNodes()
    res=obj.mergeNodes(lists)
    while res:
        print(res.val,end=" -> ")
        res=res.next
    print("None")