109-convert_sorted_list_to_binary_search_tree
#############################################

:date: 2015-11-26 22:40
:tags: Binary Search Trees, Recursion
:category: LeetCode
:slug: 109-convert_sorted_list_to_binary_search_tree

`LeetCode Problem Link <https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/>`_

The top to bottom recursive approach is trivial. At the beginning of each call, we have to get to the middle of
list. So the time complexity is O(nlogn).

.. code-block:: java

    // convert it to a height balanced BST
    public TreeNode sortedListToBST(ListNode head) {

        if (head == null)
            return null;

        int n = 0;

        ListNode cur = head;

        do {
            n++;
            cur = cur.next;
        } while (cur != null);

        int steps = n/2;

        cur = head;

        ListNode prev = null;
        for (int i=0; i<steps; i++) {
            prev = cur;
            cur = cur.next;
        }

        TreeNode root = new TreeNode(cur.val);
        if (prev != null) {
            prev.next = null;
            root.left = sortedListToBST(head);
        }

        if (cur.next != null) {
            root.right = sortedListToBST(cur.next);
        }

        return root;
    }

Now we can build the BST from bottom up. This is pretty tricky. We have to have a pointer to keep track where exactly ]]
we are currently at in the singly linked list.

.. code-block:: java

    // convert it to a height balanced BST
    public TreeNode sortedListToBST(ListNode head) {

        if (head == null)
            return null;

        int n = 0;

        ListNode cur = head;
        do {
            n++;
            cur = cur.next;
        } while (cur != null);

        // where in the singly linked list we're at right now
        ListNode[] list = new ListNode[1];
        list[0] = head;

        TreeNode root = sortedListToBST(list, 0, n-1);

        return root;
    }

    private TreeNode sortedListToBST(ListNode[] list, int low, int high) {

        int middle = low + (high-low)/2;

        TreeNode left = null;

        if (middle - 1 >= low)
            left = sortedListToBST(list, low, middle - 1);

        TreeNode node = new TreeNode(list[0].val);
        list[0] = list[0].next;

        TreeNode right = null;

        if (middle + 1 <= high)
            right = sortedListToBST(list, middle + 1, high);

        node.left = left;
        node.right = right;
        return node;
    }

From http://articles.leetcode.com/2010/11/convert-sorted-list-to-balanced-binary.html

 The list’s length could be found in O(N) time by traversing the entire list’s once.
 The recursive calls traverse the list and create tree’s nodes by the list’s order, which also takes O(N) time.
 Therefore, the overall run time complexity is still O(N).