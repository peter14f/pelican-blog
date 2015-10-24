019-remove_nth_node_from_end_of_list
####################################

:date: 2015-09-07 20:21
:tags: Linked Lists
:category: LeetCode
:slug: 019-remove_nth_node_from_end_of_list

`LeetCode Problem Link <https://leetcode.com/problems/remove-nth-node-from-end-of-list/>`_

The one pass solution may be quite hard to come up with if you are not thinking toward the right direction.


I am going to give the two pass solution first.
In the first pass, I count the number of nodes. In the second pass, I skip the nth node from the end of the list

.. code-block:: java

    public ListNode removeNthFromEnd(ListNode head, int n) {

        if (head==null)
            return head;

        int x=0;

        ListNode cur = head;
        while (cur!=null) {
            x++;
            cur = cur.next;
        }

        cur = head;
        if (n==x) {
            return head.next;
        }

        int i=x;
        while (cur!=null) {
            if (i == n + 1) {
                cur.next = cur.next.next;
                break;
            }
            cur = cur.next;
            i--;
        }
        return head;
    }

The one pass solution involves using three pointers: ``prev``, ``cur``, ``tail``. The first thing we need to do is
to make sure that tail is ``n-1`` nodes after ``cur``. And the We move all three pointers forward until ``tail`` is
the last node in the list.

Now we know ``cur`` needs to be removed.

.. code-block:: java

    public ListNode removeNFromEnd(ListNode head, int n) {

        ListNode prev = null;
        ListNode cur = head;
        ListNode tail = head;

        for (int i=0; i < n-1; i++) {
            tail = tail.next;
        }


        while (tail.next != null) {
            prev = cur;
            cur = cur.next;
            tail = tail.next;
        }

        if (prev == null) {
            return cur.next;
        }
        else {
            prev.next = cur.next;
        }

        return head;
    }