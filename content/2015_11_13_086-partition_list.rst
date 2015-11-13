086-partition_list
##################

:date: 2015-11-13 14:43
:tags: Linked List
:category: LeetCode
:slug: 086-partition_list

`LeetCode Problem Link <https://leetcode.com/problems/partition-list/>`_

Go through all nodes in the linked list and maintain two lists, one called ``leftList``, the other one called
``rightList``. In ``leftList``, I insert the
nodes that have values smaller than ``x``. In ``rightList``, I insert node that have values equal to or larger than
``x``. Link ``rightList`` to the end of ``leftList``.

.. code-block:: java

    public ListNode partition(ListNode head, int x) {

        if (head==null)
            return null;

        // smallList head and tail
        ListNode leftListHead = null;
        ListNode leftListTail = null;

        // rightList head and tail
        ListNode rightListHead = null;
        ListNode rightListTail = null;

        ListNode cur = head;

        while (cur != null) {
            ListNode oldNext = cur.next;

            if (cur.val < x) {
                // add to leftList

                if (leftListTail == null) {
                    // list is empty
                    leftListHead = cur;
                    leftListTail = cur;
                    leftListTail.next = null;
                }
                else {
                    leftListTail.next = cur;
                    leftListTail = cur;
                    leftListTail.next = null;
                }
            }
            else {
                // add to rightList

                if (rightListTail == null) {
                    // list is empty
                    rightListHead = cur;
                    rightListTail = cur;
                    rightListTail.next = null;
                }
                else {
                    rightListTail.next = cur;
                    rightListTail = cur;
                    rightListTail.next = null;
                }
            }

            cur = oldNext;
        }

        if (leftListTail != null) {
            leftListTail.next = rightListHead;
            return leftListHead;
        }
        else {
            return rightListHead;
        }
    }