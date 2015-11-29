117-populating_next_right_pointers_in_each_node_ii
##################################################

:date: 2015-11-29 18:17
:tags: Binary Trees, Breadth First Search, Linked List
:category: LeetCode
:slug: 117-populating_next_right_pointers_in_each_node_ii

`LeetCode Problem Link <https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/>`_

Definitely solve the previous problem 116-populating_next_right_pointers_in_each_node first. The difference is now
that the new ``listHead`` may not always be the old ``listHead``'s left child. We must set it by ourselves.

The other thing that's different is connecting nodes in the next level always requires updating ``prev`` pointer.

.. code-block:: java

    public void connect(TreeLinkNode root) {

        TreeLinkNode listHead = root;

        while (listHead != null) {
            TreeLinkNode listCur = listHead;
            TreeLinkNode prev = null;
            TreeLinkNode nextListHead = null;

            while (listCur != null) {


                if (listCur.left != null) {
                    if (prev != null) {
                        prev.next = listCur.left;
                        prev = prev.next;
                    }
                    else {
                        prev = listCur.left;
                        nextListHead = prev;
                    }
                }

                if (listCur.right != null) {
                    if (prev != null) {
                        prev.next = listCur.right;
                        prev = prev.next;
                    }
                    else {
                        prev = listCur.right;
                        nextListHead = prev;
                    }
                }

                listCur = listCur.next;
            }

            listHead = nextListHead;
        }
    }

