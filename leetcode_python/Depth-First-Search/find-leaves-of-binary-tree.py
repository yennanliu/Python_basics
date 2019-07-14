# V0 

# V1 
# https://blog.csdn.net/danspace1/article/details/87738403
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root: 'TreeNode') -> 'List[List[int]]':
        def getLevel(root, d):
            if not root:
                return 0
            left = getLevel(root.left, d)
            right = getLevel(root.right, d)
            level = 1 + max(left, right)
            d[level].append(root.val)
            return level
        
        d = collections.defaultdict(list)
        getLevel(root, d)
        res = []
        for k in sorted(d.keys()):
            res.append(d[k])
        return res

# V1' 
# https://blog.csdn.net/danspace1/article/details/87738403
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        d = collections.defaultdict(list)
        ans = []
        
        def traverse(root):
            # return the level of the nodes
            if not root:
                return 0
            left = traverse(root.left)
            right = traverse(root.right)
            level = max(left, right) + 1
            d[level].append(root.val)
            return level
        
        traverse(root)
        for i in range(1, len(d)+1):
            ans.append(d[i])
        return ans

# V2 
# Time:  O(n)
# Space: O(h)
class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def findLeavesHelper(node, result):
            if not node:
                return -1
            level = 1 + max(findLeavesHelper(node.left, result), \
                            findLeavesHelper(node.right, result))
            if len(result) < level + 1:
                result.append([])
            result[level].append(node.val)
            return level

        result = []
        findLeavesHelper(root, result)
        return result
