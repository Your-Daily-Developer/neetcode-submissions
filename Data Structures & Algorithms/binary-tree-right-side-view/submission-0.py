class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def dfs(node, depth):
            if not node:
                return
            # first time we reach this depth → it's the rightmost so far
            if depth == len(result):
                result.append(node.val)
            
            # go right first, then left
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        
        dfs(root, 0)
        return result