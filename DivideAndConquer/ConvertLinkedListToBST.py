# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        def findMid(head) : 
            prev = None
            fastPt, mid = head, head
            while fastpt and fastpt.next:
                prev= mid
                mid = mid.next
                fastpt = fastpt.next.next
            prev.next = None
            return mid
        
        def helper(head):
            if not head:
                return None
            if not head.next:
                return TreeNode(head.val)
            
            mid = findMid(head)
            
            node = TreeNode(mid.val)
            node.left = helper(head)
            node.right = helper(mid.next)
            
            return node
        
        return helper(head)