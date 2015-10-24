021-merge_two_sorted_lists
##########################

:date: 2015-09-07 20:23
:tags: Linked Lists
:category: LeetCode
:slug: 021-merge_two_sorted_lists

`LeetCode Problem Link <https://leetcode.com/problems/merge-two-sorted-lists/>`_

Merging two sorted linked lists.

.. code-block:: java

    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {

        if (l1==null)
            return l2;
        if (l2==null)
            return l1;

        ListNode cur1 = l1;
        ListNode cur2 = l2;
        ListNode head;
        ListNode tail;

        if (cur1.val <= cur2.val) {
            head = cur1;
            tail = cur1;
            cur1 = cur1.next;
        }
        else {
            head = cur2;
            tail = cur2;
            cur2 = cur2.next;
        }

        while (cur1 != null && cur2 != null) {
            if (cur1.val <= cur2.val) {
                tail.next = cur1;
                tail = cur1;
                cur1 = cur1.next;
            }
            else {
                tail.next = cur2;
                tail = cur2;
                cur2 = cur2.next;
            }

            tail.next = null;
        }

        if (cur1 != null) {
            tail.next = cur1;
        }
        else if (cur2 != null){
            tail.next = cur2;
        }

        return head;
    }