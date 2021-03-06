"""

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the 
root node down to the farthest leaf node.

 

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:

Input: root = [1,null,2]
Output: 2

Example 3:

Input: root = []
Output: 0

Example 4:

Input: root = [0]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100

"""

# V0
# IDEA : DFS
class Solution(object):
    def maxDepth(self, root):

        if root == None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# V0'
# IDEA : DFS
class Solution:
    def maxDepth(self, root):
        self.layer_final = 0
        self.dfs(root, 0, self.layer_final)
        return self.layer_final
        
    def dfs(self, root, layer, layer_final):
        if root:
            if layer + 1 > layer_final:
                self.layer_final += 1
            self.dfs(root.left,  layer + 1, self.layer_final)
            self.dfs(root.right, layer + 1, self.layer_final)
            
# V1
# https://blog.csdn.net/coder_orz/article/details/51337420
# IDEA : DFS
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

### Test case  (TODO : write test for tree data structure)
s=Solution()
assert s.maxDepth([3,9,20,None,None,15,7]) == 3 
assert s.maxDepth([]) == 0
assert s.maxDepth([1]) == 1 
assert s.maxDepth([1,2,3]) == 2
assert s.maxDepth([1,2,3,4,5]) == 3

# V1'
# https://blog.csdn.net/coder_orz/article/details/51337420
# IDEA : BFS
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

        depth = 0
        q = [root]
        while len(q) != 0:
            depth += 1
            for i in range(0, len(q)):
                if q[0].left:
                    q.append(q[0].left)
                if q[0].right:
                    q.append(q[0].right)
                del q[0]
        return depth

# V1''
# https://blog.csdn.net/qqxx6661/article/details/75676272
class Solution(object):
    level_true = 0
    def preorder(self, root, level, level_true):
        if root:
            if level_true < level+1: 
                #print(level_true)
                self.level_true += 1
            self.preorder(root.left, level+1, self.level_true)
            self.preorder(root.right, level+1, self.level_true)
    def maxDepth(self, root):
        self.preorder(root, 0, self.level_true)
        return self.level_true

# V2
# Time:  O(n)
# Space: O(h), h is height of binary tree
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
