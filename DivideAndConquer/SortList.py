# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next :
            return head
        
        # Divide, get Middle
        mid = self.getMiddle(head)
        
        # Sort
        left = self.sortList(head)
        right = self.sortList(mid)
        
        # Merge
        return self.merge(left,right)
        
        
    def getMiddle(self, head):
        prevMid = None
        while head and head.next:
            prevMid = head if not prevMid else prevMid.next
            head = head.next.next
        
        mid = prevMid.next
        prevMid.next=None
        return mid
    
    def merge(self,l1,l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val<l2.val:
            l1.next = self.merge(l1.next,l2)
            return l1
        else:
            l2.next = self.merge(l2.next,l1)
            return l2