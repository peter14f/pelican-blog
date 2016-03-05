094-binary_tree_inorder_traversal
#################################

:date: 2015-11-18 18:06
:tags: Binary Trees, Tree Traversal, Inorder Traversal
:category: LeetCode
:slug: 094-binary_tree_inorder_traversal

`LeetCode Problem Link <https://leetcode.com/problems/binary-tree-inorder-traversal/>`_

I solved this problem using a stack and a while loop.

.. code-block:: java

    public List<Integer> inorderTraversal(TreeNode root) {

        List<Integer> ans = new ArrayList<Integer>();

        if (root==null)
            return ans;

        Stack<TreeNode> stk = new Stack<TreeNode>();

        stk.push(root);
        TreeNode cur = root.left;

        while (cur != null || !stk.isEmpty()) {

            if (cur != null) {
                stk.push(cur);
                cur = cur.left;
            }
            else {
                TreeNode top = stk.pop();
                ans.add(top.val);
                cur = top.right;
            }
        }

        return ans;
    }

There is also the morris traversal which is O(1) space.

