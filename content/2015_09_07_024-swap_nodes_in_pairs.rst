024-swap_nodes_in_pairs
#######################

:date: 2015-09-07 20:26
:tags: Linked Lists
:category: LeetCode
:slug: 024-swap_nodes_in_pairs

`LeetCode Problem Link <https://leetcode.com/problems/swap-nodes-in-pairs/>`_

The problem is not so hard, but manipulating linked lists always requires care. Is the list properly null-terminated?
The next problem is the more difficult one.

.. code-block:: java

    public ListNode swapPairs(ListNode head) {

        ListNode cur = head;

        if (head == null || head.next == null) {
            return head;
        }

        ListNode newHead = cur.next;
        ListNode prev = null;

        while (cur != null) {
            ListNode oldNext = cur.next;

            if (prev != null)
                prev.next = oldNext;

            if (oldNext==null) {
                if (prev != null) {
                    prev.next = cur;
                    // cur.next is null already
                    // cur is the last node in the linked list
                }
                break;
            }

            ListNode newNext = oldNext.next;
            oldNext.next = cur;
            cur.next = null; // null terminate the linked list

            prev = cur;
            cur = newNext;
        }

        return newHead;
    }