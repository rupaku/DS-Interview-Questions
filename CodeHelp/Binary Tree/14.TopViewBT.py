'''
https://practice.geeksforgeeks.org/problems/top-view-of-binary-tree/1
'''
class Solution:
    
    def topviewu(self,root,d,vd,lv):
        if not root:
            return
        if vd in d:
            if d[vd][0]>lv:
                d[vd]=(lv,root.data)
        else:
            d[vd]=(lv,root.data)
            
        #calling function recursively for left and right subtrees.
        self.topviewu(root.left,d,vd-1,lv+1)
        self.topviewu(root.right,d,vd+1,lv+1)
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self, root):
        
        #map to store the pair of node value and its level
        #with respect to the vertical distance from root.
        d=dict()
        ans=[]
        self.topviewu(root,d,0,0)
        
        #traversing the map and storing the nodes in list 
        #at every horizontal distance.
        for e in sorted(d):
            ans.append(d[e][1])
            
        #returning the output list. 
        return ans
        
        