# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # max_height = 0
        # if not root:
        #     return max_height
        
        # stack = [root]
        # while stack:
        #     node = stack.pop()
        #     height += 1

        #     if node:
        #         if height > max_height:
        #             max_height = height
        #         stack.append(node.left)
        #         stack.append(node.right)
        # return max_height

        # if not root:
        #     return 0
        
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        level = 0
        if not root:
            return level

        queue = deque([root])

        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return level