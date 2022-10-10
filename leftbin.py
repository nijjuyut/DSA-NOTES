def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def height(root):
            if root is None:
                return 0
            lheight=height(root.left)
            rheight=height(root.right)
            if lheight>rheight:
                return lheight+1
            else:
                return rheight+1
        def levelorder(root,h,l):
            if root is None:
                return
            elif h==1:
                l.append(root.val)
            elif h>1:
                levelorder(root.left,h-1,l)
                levelorder(root.right,h-1,l)
        
        ans=[]
        n=height(root)
        for i in range(1,n+1):
            l=[]
            levelorder(root,i,l)
            ans.append(l[-1])
        return ans
