116-populating_next_right_pointers_in_each_node
###############################################

:date: 2015-11-29 16:09
:tags: Binary Trees, Breadth First Search, Linked Lists
:category: LeetCode
:slug: 116-populating_next_right_pointers_in_each_node

`LeetCode Problem Link <https://leetcode.com/problems/distinct-subsequences/>`_

If we were allowed using non-constant extra space, we could use the way we solved 102-binary_tree_level_order_traversal.
Since we are allowed only constant space.

We cannot use recursion either since the calls on the stack counts toward space usage as well.

Here is my solution. It is basically still using BFS but since the cur nodes in the previous level have already
been linked together, there is no need to use a list.

.. code-block:: java

        public void connect(TreeLinkNode root) {

        if (root == null)
            return;

        TreeLinkNode listHead = root;

        while (listHead != null) {
            TreeLinkNode listCur = listHead;
            TreeLinkNode prev = null;

            while (listCur != null) {


                if (listCur.left != null) {

                    if (prev != null)
                        prev.next = listCur.left;

                    listCur.left.next = listCur.right;
                    prev = listCur.right;
                }

                listCur = listCur.next;
            }

            listHead = listHead.left;
        }
    }