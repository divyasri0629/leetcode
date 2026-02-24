class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:

        def solve(node, number):
            if not node:
                return 0

            # same as building number along indices
            number = number * 2 + node.val

            # leaf (no children)
            if node.left is None and node.right is None:
                return number

            # like going to 2*i+1 and 2*i+2
            left_sum = solve(node.left, number)
            right_sum = solve(node.right, number)

            return left_sum + right_sum

        return solve(root, 0)
        