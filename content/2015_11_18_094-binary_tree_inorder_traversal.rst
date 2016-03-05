094-binary_tree_inorder_traversal
#################################

:date: 2015-11-18 18:06
:tags: Binary Trees, Binary Tree Traversal, Inorder Traversal
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

Here is the basic idea, if ``cur`` has a left child, the inorder predecessor's right child either needs
to be set to ``cur`` or restored back to ``null``

::

         cur                                     cur
         2                   2                    2                     2
        / \                 /| \                 / \                   / \
       1   3          cur  1--  3               1   3                 1   3 cur
                          output 1              output 2                output 3
                    1's right child is 2   1's right child is null


I find it very difficult to remember the implementation. Remembering the picture is probably way easier.


.. code-block:: java

    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> ans = new ArrayList<Integer>();

        TreeNode cur = root;

        while (cur != null) {
            if (cur.left != null) {
                TreeNode inorderPred = cur.left;

                while (inorderPred.right != null && inorderPred.right != cur){
                    inorderPred = inorderPred.right;
                }

                if (inorderPred.right == null) {
                    inorderPred.right = cur;
                    cur = cur.left;
                }
                else {
                    inorderPred.right = null;
                    ans.add(cur.val);
                    cur = cur.right;
                }
            }
            else {
                ans.add(cur.val);
                cur = cur.right;
            }
        }

        return ans;
    }
