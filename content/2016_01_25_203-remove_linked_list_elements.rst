203-remove_linked_list_elements
###############################

:date: 2016-1-25 20:18
:tags: Linked Lists
:category: LeetCode
:slug: 203-remove_linked_list_elements

`LeetCode Problem Link <https://leetcode.com/problems/remove-linked-list-elements/>`_

We are removing all elements that have the target value in a singly-linked lists.

.. code-block:: java

    public ListNode removeElements(ListNode head, int val) {

        if (head == null)
            return null;

        while (head != null && head.val == val) {
            head = head.next;
        }

        if (head == null)
            return null;

        ListNode prev = null;
        ListNode cur = head;

        while (cur != null) {
            ListNode origNext = cur.next;

            if (cur.val == val)
                prev.next = cur.next;
            else
                prev = cur;

            cur = origNext;
        }

        return head;
    }

This takes O(n) time where ``n`` is the length of the original list. We can do this in one-pass.
