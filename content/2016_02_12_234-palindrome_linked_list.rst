234-palindrome_linked_list
##########################

:date: 2016-2-12 17:07
:tags: Palindromes, Linked Lists
:category: LeetCode
:slug: 234-palindrome_linked_list

`LeetCode Problem Link <https://leetcode.com/problems/palindrome-linked-list/>`_

The first solution using a stack is the most straightforward one. It takes O(n) time and O(n) space.

.. code-block:: java

    public boolean isPalindrome(ListNode head) {
        if (head == null)
            return true;

        Stack<ListNode> stk = new Stack<ListNode>();

        ListNode tail = head;

        while (tail != null) {
            stk.push(tail);
            tail = tail.next;
        }

        ListNode cur = head;

        while (!stk.isEmpty()) {
            ListNode node = stk.pop();
            if (node.val != cur.val)
                return false;
            cur = cur.next;
        }

        return true;
    }

The second solution uses recursion and no extra space. But technically the functions calls on the call stack
should still count toward the memory usage. So this still takes O(n) time and O(n) space.

.. code-block:: java

    public boolean isPalindrome(ListNode head) {
        if (head==null)
            return true;

        ListNode[] cur = {head};

        return isPalindrome(cur, head);
    }

    private boolean isPalindrome(ListNode[] cur, ListNode node) {
        if (node.next==null) {
            return cur[0].val == node.val;
        }
        else {
            boolean r = isPalindrome(cur, node.next);
            cur[0] = cur[0].next;
            if (r)
                return cur[0].val == node.val;
            else
                return false;
        }
    }

How in the world can we solve this in O(n) time and O(1) space as asked in the follow-up?

We need to be a little more clever.

Step1: Find the middle node of the list.
Step2: Reverse the sublist starting at the mid point.
Step3: Compare the two lists up to the length of the reversed list.
Step4: (Optional) We can restore the linked list back its original state.

Just remember to use the iterative approach when reversing the linked list. Otherwise it defeat the purpose. Remember
that the recursive calls on the call stack also counts toward memory usage.

.. code-block:: java

    public boolean isPalindrome(ListNode head) {
        if (head==null || head.next==null)
            return true;

        ListNode slow = head;
        ListNode fast = head.next;

        while (fast != null && fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        ListNode p = slow.next;
        ListNode prev = null;

        while (p != null) {
            ListNode origNext = p.next;
            p.next = prev;
            prev = p;
            p = origNext;
        }

        ListNode head2 = prev;
        ListNode p2 = head2;
        p = head;

        boolean result = true;

        // comparison
        while (p != null && p2 != null) {
            if (p.val != p2.val) {
                result = false;
                break;
            }

            p = p.next;
            p2 = p2.next;
        }

        // restore the list to its original state
        prev = null;
        p2 = head2;

        while (p2 != null) {
            ListNode origNext = p2.next;
            p2.next = prev;
            prev = p2;
            p2 = origNext;
        }

        slow.next = prev;

        return result;
    }