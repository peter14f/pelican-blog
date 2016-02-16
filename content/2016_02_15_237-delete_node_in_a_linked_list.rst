237-delete_node_in_a_linked_list
################################

:date: 2016-2-15 23:43
:tags: Singly Linked Lists
:category: LeetCode
:slug: 237-delete_node_in_a_linked_list

`LeetCode Problem Link <https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/>`_

The problem requires that you think outside of the box. You only have access to the nodes starting at the
node you want to delete. So all we can do is copy the values from the following nodes.

.. code-block:: java

    public void deleteNode(ListNode node) {

        if (node == null)
            return;

        ListNode cur = node;
        ListNode prev = null;

        while (cur != null) {
            if (cur.next == null && prev != null) {
                prev.next = null;
            }
            else {
                cur.val = cur.next.val;
            }

            prev = cur;
            cur = cur.next;
        }
    }

It's impossible to delete if the node given is the tail node.
