025-reverse_nodes_in_k_group
############################

:date: 2015-09-07 20:27
:tags: Linked Lists, Linked List Reversal
:category: LeetCode
:slug: 025-reverse_nodes_in_k_group

`LeetCode Problem Link <https://leetcode.com/problems/reverse-nodes-in-k-group/>`_

A good review before doing this problem is 206-reverse_linked_list.

One way to do this problem is maintain a ``tail`` pointer who is always ``k-1`` nodes behind ``cur``.

A better way is to simply count as ``cur`` moves forward.

One gatta is check for the case where ``k > n`` where ``n`` is the length of the linked list.

.. code-block:: java

    public ListNode reverseKGroup(ListNode head, int k) {

        int i=0;
        ListNode cur = head;
        ListNode newHead = null;
        ListNode sublistHead = head;
        ListNode newSublistHead = null;
        ListNode prevSublistTail = null;

        while (cur != null) {
            i++;

            if (i==k) {
                ListNode oldNext = cur.next;
                newSublistHead = reverseSublist(sublistHead, cur);

                if (newHead == null) {
                    newHead = newSublistHead;
                }
                else {
                    prevSublistTail.next = newSublistHead;
                }

                cur = oldNext;
                prevSublistTail = sublistHead;
                sublistHead = cur;
                i=0;
            }
            else {
                cur = cur.next;
            }
        }

        if (i != 0 && prevSublistTail != null) {
            prevSublistTail.next = sublistHead;
        }

        // this must be because k > n
        if (newHead==null)
            return head;
        return newHead;
    }

    public ListNode reverseSublist(ListNode head, ListNode tail) {

        if (head==null || head==tail)
            return head;

        ListNode cur = head;
        ListNode prev = null;

        while (cur != null) {
            ListNode oldNext = cur.next;
            cur.next = prev;

            if (cur==tail)
                break;

            prev = cur;
            cur = oldNext;
        }

        return tail;
    }

The previous problem is a specific case of this problem. If we set ``k`` to 2, we would also get a solution
to the previous problem.