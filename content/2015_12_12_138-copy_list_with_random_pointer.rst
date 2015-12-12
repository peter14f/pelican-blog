138-copy_list_with_random_pointer
#################################

:date: 2015-12-12 12:35
:tags: Linked Lists
:category: LeetCode
:slug: 138-copy_list_with_random_pointer

`LeetCode Problem Link <https://leetcode.com/problems/copy-list-with-random-pointer/>`_

For each node in the original list append a duplicated node.

Copy the random pointer as well.

This is the first pass.

In the second pass, we correct the random pointers for every other node on the list. Advance the random pointers by
one node. Notice how these random pointer point to the duplicated nodes now.

In the third pass, we separate the original nodes from the duplicated nodes.

Then we can simply return the head of the duplicated list.

.. code-block:: java

    public RandomListNode copyRandomList(RandomListNode head) {

        if (head == null)
            return null;

        RandomListNode cur = head;
        RandomListNode newListHead = null;

        while (cur != null) {
            RandomListNode oldNext = cur.next;
            RandomListNode dup = new RandomListNode(cur.label);

            if (newListHead == null)
                newListHead = dup;

            dup.next = cur.next;
            dup.random = cur.random;

            cur.next = dup;

            cur = oldNext;
        }

        cur = head;

        while (cur != null) {
            RandomListNode origNext = cur.next.next;
            if (cur.next.random != null)
                cur.next.random = cur.next.random.next;
            cur = origNext;
        }

        cur = head;
        while (cur != null) {
            RandomListNode origNext = cur.next.next;

            if (origNext != null)
                cur.next.next = origNext.next;

            cur.next = origNext;
            cur = origNext;
        }

        return newListHead;
    }

This takes O(n) time.
