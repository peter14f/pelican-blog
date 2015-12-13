142-linked_list_cycle_ii
########################

:date: 2015-12-13 15:38
:tags: Linked List, Linked List Cycle
:category: LeetCode
:slug: 142-linked_list_cycle_ii

`LeetCode Problem Link <https://leetcode.com/problems/linked-list-cycle-ii/>`_

The implementation for this problem is not difficult. Once ``fast`` catches up with ``slow``, at location ``x``.
We set ``cur`` to the head of the list and then try to advance both ``x`` and ``cur`` at the same rate.
The location where ``x`` meets with ``cur`` is the start of the cycle.

We can show why this is the case with some modular arithmetic. Let's say it takes ``x`` steps for ``slow`` to
reach the start of the cycle at which point ``fast`` has take ``2x`` steps in total and has taken ``x`` steps
since it entered the cycle.

Keep in mind ``slow`` is now at ``0 mod m``, the start of the cycle and ``fast`` is now at ``x mod m``, somewhere
within the cycle. ``m`` is just the size of the cycle. Now let's say after ``slow`` taking ``y`` steps, the two pointers finally meet. ``slow`` is at
``y mod m`` and ``fast`` is at ``(x + 2y) mod m``. These two values are actually at the same spot.

So ``y mod m`` = ``(x + 2y) mod m``

Now the question wants us to find out the beginning of the cycle which is ``0 mod m``.
``0 mod m`` = ``(x + y) mod m``.

That means if we just take another ``x`` steps from where the two pointers meet, we will be at the start of the
cycle. ``x`` is the distance from head to the start of the cycle.

.. code-block:: java

    public ListNode detectCycle(ListNode head) {
        if (head == null)
            return null;

        ListNode slow = head;
        ListNode fast = head;
        boolean hasCycle = false;

        while (slow != null) {
            boolean fastAdvancedTwice = false;

            slow = slow.next;

            if (fast!=null)
                fast = fast.next;
            if (fast!=null) {
                fast = fast.next;
                fastAdvancedTwice = true;
            }

            if (fastAdvancedTwice && fast==slow) {
                hasCycle = true;
                break;
            }

            if (!fastAdvancedTwice)
                break;
        }

        if (!hasCycle)
            return null;

        ListNode cur = head;

        while (cur != null) {
            if (cur==slow)
                return cur;

            cur = cur.next;
            slow = slow.next;
        }

        return cur;
    }

