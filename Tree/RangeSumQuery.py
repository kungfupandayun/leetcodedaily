# Segment tree node
class Node(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None
        
class NumArray:
    def __init__(self,nums):
        def createTree(nums,l,r):
            if l>r:
                return None
            if l==r:
                n=Node(l,r)
                n.total=nums[l]
                return n
            mid = (l+r)//2
            root = Node(l,r)
            root.left = createTree(nums,l,mid)
            root.right = createTree(nums,mid+1,r)
            root.total = root.left.total+root.right.total
            
            return root
        self.root = createTree(nums,0,len(nums)-1)
        

    def update(self, index: int, val: int) -> None:
        def updateTree(root,index,val):
            if root.start==root.end:
                if root.start == index:
                    root.total = val
                return root.total
            
            mid = (root.start+root.end)//2
            
            if index<=mid :
                updateTree(root.left,index,val)
            else:
                updateTree(root.right,index,val)
            root.total = root.left.total+ root.right.total 
        return updateTree(self.root,index,val)
    
    def sumRange(self, left: int, right: int) -> int:
        def sumTreeRange(root,left,right):
            if root.start==left and root.end ==right:
                return root.total
            mid = (root.start+root.end)//2
            if right<=mid:
                return sumTreeRange(root.left,left,right)
            elif left>=mid+1:
                return sumTreeRange(root.right,left,right)
            else:
                return sumTreeRange(root.left,left,mid) + sumTreeRange(root.right,mid+1,right)
            
        return sumTreeRange(self.root, left, right)