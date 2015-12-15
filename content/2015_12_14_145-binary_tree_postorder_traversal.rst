145-binary_tree_postorder_traversal
###################################

:date: 2015-12-14 20:57
:tags: Binary Trees, Binary Tree Traversals, Postorder Traversal
:category: LeetCode
:slug: 145-binary_tree_postorder_traversal

`LeetCode Problem Link <https://leetcode.com/problems/binary-tree-postorder-traversal/>`_

This is the hardest iterative traversal using a stack.

The check ``top.right!=null && prev == top.left`` won't work because ``top`` node may not have a left child.

.. code-block:: java

    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> nodes = new ArrayList<Integer>();

        Stack<TreeNode> stk = new Stack<TreeNode>();
        TreeNode cur = root;
        TreeNode prev = null;

        while (cur != null || !stk.isEmpty()) {

            if (cur != null) {
                stk.push(cur);
                cur = cur.left;
            }
            else {
                TreeNode top = stk.peek();

                if (top.right != null && prev != top.right) {
                    cur = top.right;
                }
                else
                {
                    stk.pop();
                    nodes.add(top.val);
                    prev = top;
                }
            }

        }

        return nodes;
    }
