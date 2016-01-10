160-intersection_of_two_linked_lists
####################################

:date: 2016-1-8 18:55
:tags: Linked Lists
:category: LeetCode
:slug: 160-intersection_of_two_linked_lists

`LeetCode Problem Link <https://leetcode.com/problems/intersection-of-two-linked-lists/>`_

Get the length of list A and list B first. Advance the longer list pointer such that two pointers have the same list
lengths. Start advancing two pointers until the common node is found. This takes O(n) time and O(1) space.

.. code-block:: java

    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        int aLength = 0;
        int bLength = 0;

        ListNode cur = headA;

        while (cur != null) {
            aLength++;
            cur = cur.next;
        }

        cur = headB;

        while (cur != null) {
            bLength++;
            cur = cur.next;
        }

        if (aLength > bLength) {
            int diff = aLength - bLength;

            while (diff > 0) {
                headA = headA.next;
                diff--;
            }
        }
        else if (bLength > aLength) {
            int diff = bLength - aLength;

            while (diff > 0) {
                headB = headB.next;
                diff--;
            }
        }

        while (headA != null) {
            if (headA == headB) {
                return headA;
            }

            headA = headA.next;
            headB = headB.next;
        }

        return null;
    }
