141-linked_list_cycle
#####################

:date: 2015-12-13 14:53
:tags: Linked Lists, Linked List Cycle
:category: LeetCode
:slug: 141-linked_list_cycle

`LeetCode Problem Link <https://leetcode.com/problems/word-break-ii/>`_

Use two pointers, ``fast`` and ``slow`` both start at the head of the list. Make ``fast`` take two steps
and ``slow`` take one step in each iteration. If there's a cycle in the linked list. The ``fast`` pointer
will eventually catch up with the ``slow`` pointer.

.. code-block:: java

    public boolean hasCycle(ListNode head) {
        if (head==null)
            return false;

        ListNode fast = head;
        ListNode slow = head;

        while (slow != null) {
            boolean fastAdvancedTwice = false;

            slow = slow.next;

            if (fast != null)
                fast = fast.next;
            if (fast != null) {
                fast = fast.next;
                fastAdvancedTwice = true;
            }

            if (fastAdvancedTwice && fast == slow)
                return true;

            if (!fastAdvancedTwice)
                break;
        }

        return false;
    }