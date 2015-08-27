002 Add Two Numbers
###################

:date: 2015-8-27 17:10
:tags:
:category:
:slug: 002-add-two-numbers

`LeetCode Problem Link <https://leetcode.com/problems/add-two-numbers/>`_

The problem is not difficult. But on the first try I did not take care of the case when the sum of the most
digits exceed 9. In other words, for the case of 5 + 5, my result LinkedList only contains one node with value zero.

This needs to be taken care of *after* the while loop that finished traversing the two lists.

The time complexity is obviously O(n) where n is the size of the longer list.

.. code-block:: java

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode cur1 = l1; // the head is the least significant digit
        ListNode cur2 = l2;
        ListNode sumListHead = null;
        ListNode sumListTail = null;

        boolean carry = false;

        while (cur1 != null || cur2 != null) {
            ListNode sumListNode = new ListNode(0);

            if (cur1 != null) {
                sumListNode.val += cur1.val;
                cur1 = cur1.next;
            }

            if (cur2 != null) {
                sumListNode.val += cur2.val;
                cur2 = cur2.next;
            }

            if (carry) {
                sumListNode.val++;
            }

            if (sumListNode.val > 9) {
                carry = true;
                sumListNode.val -= 10;
            }
            else {
                carry = false;
            }

            if (sumListTail == null) {
                // nothing inserted yet
                sumListHead = sumListNode;
                sumListTail = sumListNode;
            }
            else {
                // insert new node at tail, update tail
                sumListTail.next = sumListNode;
                sumListTail = sumListTail.next;
            }
        }

        if (carry) {
            ListNode sumListNode = new ListNode(1);
            sumListTail.next = sumListNode;
        }

        return sumListHead;
    }
