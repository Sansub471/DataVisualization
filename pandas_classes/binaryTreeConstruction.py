# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def makeTree(self, preorder, preOrderIndex, inStart, inEnd, inorderMap):
        if inStart > inEnd:
            return None
        
        # Get the root value and increment preOrderIndex
        root_val = preorder[preOrderIndex[0]]
        preOrderIndex[0] += 1
        
        # Create the root node
        root = TreeNode(root_val)
        
        # Find the index of the root in the inorder traversal
        inorder_idx = inorderMap[root_val]
        
        # Recursively build the left and right subtrees
        root.left = self.makeTree(preorder, preOrderIndex, inStart, inorder_idx - 1, inorderMap)
        root.right = self.makeTree(preorder, preOrderIndex, inorder_idx + 1, inEnd, inorderMap)
        
        return root

    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        
        # Map to store the index of each value in the inorder traversal
        inorderMap = {val: idx for idx, val in enumerate(inorder)}
        
        # Preorder index is passed as a single-element list to allow modification in recursion
        preOrderIndex = [0]
        
        # Build the tree
        return self.makeTree(preorder, preOrderIndex, 0, len(inorder) - 1, inorderMap)
