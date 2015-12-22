147-insertion_sort_list
#######################

:date: 2015-12-22 13:16
:tags: Sorting, Insertion Sort
:category: LeetCode
:slug: 147-insertion_sort_list

`LeetCode Problem Link <https://leetcode.com/problems/insertion-sort-list/>`_

Insertion sort should take O(n) time only if the list is already sorted.

I find the easiest to implement this is maintain the head and tail pointers of the currently sorted list.

Inserting the node at the head or tail is easy and should only take constant time.
Use a helper method to do the implementation for inserting somewhere in the middle.

.. code-block:: java

    public ListNode insertionSortList(ListNode head) {
        if (head == null) {
            return null;
        }

        ListNode sortedHead = head;
        ListNode sortedTail = head;

        ListNode node = head.next;

        sortedTail.next = null;

        while (node != null) {
            ListNode origNext = node.next;

            if (node.val <= sortedHead.val) {
                // insert at head
                node.next = sortedHead;
                sortedHead = node;
            }
            else if (node.val >= sortedTail.val) {
                // insert at tail
                sortedTail.next = node;
                sortedTail = node;
                sortedTail.next = null;
            }
            else {
                // insert somewhere in the middle
                insert(sortedHead, node);
            }

            node = origNext;
        }

        return sortedHead;
    }

    private void insert(ListNode sortedHead, ListNode newNode) {

        ListNode cur = sortedHead;

        while (cur != null) {

            if (cur.val <= newNode.val && cur.next.val > newNode.val) {
                newNode.next = cur.next;
                cur.next = newNode;
                break;
            }

            cur = cur.next;
        }
    }

The worst case time complexity should be O(n\ :superscript: `2`).
