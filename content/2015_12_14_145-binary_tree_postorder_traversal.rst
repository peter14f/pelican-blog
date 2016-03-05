145-binary_tree_postorder_traversal
###################################

:date: 2015-12-14 20:57
:tags: Binary Trees, Binary Tree Traversal, Postorder Traversal
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

Revisited the stack approach on 03/05/2016. Remembering to use ``prev`` for the postorder traversal is one thing.
Another thing to remember is that a leaf node's left child and right child will be ``null``, so make sure to check
the ``prev`` is not ``null``. Simply checking that

::

    prev == top.right

will not be enough.

The Morris traversal for postorder traversal is also the weird one. We need a dummy node and attach the
root of the tree we want to traverse to the left child of the dummy node.

We also need to write a reverse function to reverse a linked list.

::


         cur                                                                                         cur
           D                   D                    D            D                       D            D
          / |                 / |                  / |         / |                     / |           /
         2  |            cur 2  |                 2  |    cur 2  |                    2  |          2
        / \ |               /|\ |                /| \|       / \ |                   / \ |         / \
       1   3               1--  3           cur 1--  3      1    3                  1    3  cur   1   3

    3's right child is D  1's right child is 2            1's right child is null              3's right child is null
                                                    add reverse to list from 1 to 1      add reverse to list from 2 to 3



.. code-block:: java

    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> ans = new ArrayList<Integer>();

        if (root == null)
            return ans;

        TreeNode dummy = new TreeNode(0);
        dummy.left = root;

        TreeNode cur = dummy;

        while (cur != null) {

            if (cur.left != null) {

                TreeNode preorderPred = cur.left;

                while (preorderPred.right != null && preorderPred.right != cur) {
                    preorderPred = preorderPred.right;
                }

                if (preorderPred.right == null) {
                    preorderPred.right = cur;
                    cur = cur.left;
                }
                else {
                    preorderPred.right = null;
                    addInReverseOrder(ans, cur.left, preorderPred);
                    cur = cur.right;
                }
            }
            else {
                cur = cur.right;
            }
        }

        return ans;
    }

    private void addInReverseOrder(List<Integer> list, TreeNode begin, TreeNode end) {
        if (begin == end) {
            list.add(begin.val);
            return;
        }

        // reverse list
        reverse(begin, end);

        TreeNode cur = end;

        while (cur != begin) {
            list.add(cur.val);
            cur = cur.right;
        }
        list.add(cur.val);

        // restore list
        reverse(end, begin);
    }

    private void reverse(TreeNode begin, TreeNode end) {

        TreeNode prev = null;
        TreeNode cur = begin;

        while (cur != end) {
            TreeNode origNext = cur.right;

            cur.right = prev;

            prev = cur;
            cur = origNext;
        }

        cur.right = prev;
    }