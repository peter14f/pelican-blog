144-binary_tree_preorder_traversal
##################################

:date: 2015-12-14 19:48
:tags: Binary Trees, Binary Tree Traversals, Preorder Traversal, Morris Traversal
:category: LeetCode
:slug: 144-binary_tree_preorder_traversal

`LeetCode Problem Link <https://leetcode.com/problems/binary-tree-preorder-traversal/>`_

Here is the solution using a Stack. It is O(n) space complexity. In the worst case, the binary tree is a linked list.

.. code-block:: java

    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> nodes = new ArrayList<Integer>();

        TreeNode cur = root;
        Stack<TreeNode> stk = new Stack<TreeNode>();

        while (cur != null || !stk.isEmpty()) {

            if (cur != null) {
                stk.push(cur);
                nodes.add(cur.val);
                cur = cur.left;
                continue;
            }

            cur = stk.pop();
            cur = cur.right;
        }

        return nodes;
    }

Here is the solution using Morris Traversal. It takes O(1) space.

.. code-block:: java

    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> nodes = new ArrayList<Integer>();

        TreeNode cur = root;

        while (cur != null) {

            if (cur.left != null) {

                TreeNode lastNodeInLeft = cur.left;

                while (lastNodeInLeft.right != null && lastNodeInLeft.right != cur) {
                    lastNodeInLeft = lastNodeInLeft.right;
                }

                if (lastNodeInLeft.right == null) {
                    lastNodeInLeft.right = cur;

                    nodes.add(cur.val);
                    cur = cur.left;
                }
                else {
                    // note that cur is skipped since we've been here before
                    lastNodeInLeft.right = null;
                    cur = cur.right;
                }
            }
            else {
                nodes.add(cur.val);
                cur = cur.right;
            }

        }

        return nodes;
    }

Note that Morris Traversal is possible with both preorder and inoreder traversals.
