206-reverse_linked_list
#######################

:date: 2015-10-22 20:05
:tags: Linked Lists, Linked List Reversal
:category: LeetCode
:slug: 206-reverse_linked_list

`LeetCode Problem Link <https://leetcode.com/problems/reverse-nodes-in-k-group/>`_

It's probably not feasible to memorize the whole implementation. But for the iterative solution ``prev`` pointer is
needed. For the recurive solution, storing the ``oldNext`` pointer is needed. Also double check that the reversed
linked list is properly null terminated.

Iterative solution:

.. code-block:: java

    public ListNode reverseList(ListNode head) {

        if (head==null)
            return head;

        ListNode cur = head;
        ListNode newHead = null;
        ListNode prev = null;

        while (cur!=null) {
            ListNode oldNext = cur.next;
            cur.next = prev;
            if (oldNext == null)
                newHead = cur;
            prev = cur;
            cur = oldNext;
        }

        return newHead;
    }




Recursive solution:

.. code-block:: java

    public ListNode reverseListRec(ListNode head) {
        if (head==null || head.next == null)
            return head;

        ListNode oldNext = head.next;
        ListNode newHead = reverseListRec(head.next);
        oldNext.next = head;
        head.next = null;
        return newHead;
    }