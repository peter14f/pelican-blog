082-remove_duplicates_from_sorted_list_ii
#########################################

:date: 2015-11-11 20:32
:tags: Remove Duplicates, Sorted List
:category: LeetCode
:slug: 082-remove_duplicates_from_sorted_list_ii

`LeetCode Problem Link <https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/>`_

What does it mean to be a distinct node in a sorted list? It's not the same as its previous node (if previous node
exists) and it's not the same as its next node (if next node exists).

And the I maintain the head and tail of this new list, so that I can easily add the newly found distinct node at the
end of this new list.

.. code-block:: java

    public ListNode deleteDuplicates(ListNode head) {

        if (head==null)
            return null;

        ListNode prev = null;
        ListNode cur = head;

        ListNode sortedListHead = null;
        ListNode sortedListTail = null;

        while (cur != null) {
            ListNode next = cur.next;
            ListNode newDistinctNode = null;

            if (prev != null && next != null) {
                if (cur.val != next.val && prev.val != cur.val)
                    newDistinctNode = cur;
            }
            else if (prev == null && next != null) {
                if (cur.val != next.val)
                    newDistinctNode = cur;
            }
            else if (next == null && prev != null) {
                if (cur.val != prev.val)
                    newDistinctNode = cur;
            }
            else {
                newDistinctNode = cur;
            }

            prev = cur;
            cur = next;

            if (newDistinctNode != null) {
                newDistinctNode.next = null;
                if (sortedListTail == null) {
                    sortedListHead = newDistinctNode;
                    sortedListTail = newDistinctNode;
                }
                else {
                    sortedListTail.next = newDistinctNode;
                    sortedListTail = newDistinctNode;
                }
            }
        }

        return sortedListHead;

    }

