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
        Stack<TreeNode> stk = new Stack<TreeNode>();

        TreeNode cur = root;

        while (true) {
            if (cur==null && stk.isEmpty()) {
                break;
            }

            if (cur==null) {
                cur = stk.pop();
                ans.add(cur.val);
                cur = cur.right;

            }
            else {
                stk.push(cur);
                cur = cur.left;
            }
        }

        return ans;
    }