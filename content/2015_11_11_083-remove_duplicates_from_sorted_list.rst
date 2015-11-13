083-remove_duplicates_from_sorted_list
######################################

:date: 2015-11-11 20:33
:tags: Remove Duplicates, Sorted List
:category: LeetCode
:slug: 083-remove_duplicates_from_sorted_list

`LeetCode Problem Link <https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/>`_

We're asked to keep only one node for each node in the sorted list that have duplicates.

Problem is not hard. When working wiht linked lists, always make sure that list is properly terminated.

.. code-block:: java

    public ListNode deleteDuplicates(ListNode head) {
        if (head==null) {
            return null;
        }

        ListNode cur = head;

        while (cur != null) {
            ListNode nextNode = cur.next;

            while (nextNode != null && nextNode.val == cur.val) {
                nextNode = nextNode.next;
            }

            cur.next = nextNode;
            cur = nextNode;
        }

        return head;
    }