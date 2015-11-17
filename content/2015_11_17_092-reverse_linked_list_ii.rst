092-reverse_linked_list_ii
##########################

:date: 2015-11-17 20:23
:tags: Linked Lists
:category: LeetCode
:slug: 092-reverse_linked_list_ii

`LeetCode Problem Link <https://leetcode.com/problems/reverse-linked-list-ii/>`_

I chose to do this problem iteratively. Reversing a linked list iteratively requires using a ``prev`` pointer.

.. code-block:: java

    public ListNode reverseBetween(ListNode head, int m, int n) {

        if (head == null || m==n) {
            return head;
        }

        if (m==1) {
            head = reverseBetween(head, n-m);
            return head;
        }
        else if (m > 1) {
            int i=1;
            ListNode cur = head;
            ListNode prev = null;

            do {
                prev = cur;
                cur = cur.next;
                i++;
            } while (i < m);

            prev.next = reverseBetween(cur, n-m);
            return head;
        }
        else
            throw new IllegalArgumentException();

    }

    /* Given m, n satisfy the following condition:
     *  1 ≤ m ≤ n ≤ length of list.
     */
    private ListNode reverseBetween(ListNode from, int distanceToTail) {

        int i = 0;

        ListNode cur = from;
        ListNode prev = null;

        do {
            ListNode oldNext = cur.next;

            cur.next = prev;

            prev = cur;
            cur = oldNext;

            i++;
        } while (i <= distanceToTail);

        ListNode nextSection = cur;

        ListNode newHead = prev;

        from.next = nextSection;

        return newHead;
    }