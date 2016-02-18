255-verify_preorder_sequence_in_binary_search_tree
##################################################

:date: 2016-2-18 13:34
:tags: Binary Search Trees, Inorder Traversal
:category: LeetCode
:slug: 255-verify_preorder_sequence_in_binary_search_tree

`LeetCode Problem Link <https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/>`_

In a preorder traversal sequence, the first element is always the root. The first element you find that is greater
than root marks the beginning of the right subtree. All elements starting from it must be greater than root. Then
we must use recursion to check the left subtree and the right subtree.

.. code-block:: java

    // could assume each number in the sequence is unique
    public boolean verifyPreorder(int[] preorder) {
        if (preorder.length == 0)
            return true;

        return isPreorder(preorder, 0, preorder.length - 1);
    }

    private boolean isPreorder(int[] preorder, int start, int end) {
        if (start==end)
            return true;

        int root = preorder[start];
        boolean checkLeftSubtree = true;
        boolean checkRightSubtree = true;

        int rightChildIndex = -1;

        for (int i=start+1; i<=end; i++) {
            if (preorder[i] > root) {
                rightChildIndex = i;
                break;
            }
        }

        if (rightChildIndex == -1) {
            // everyone behind root is in the left subtree
            if (start+1 <= end)
                checkLeftSubtree = isPreorder(preorder, start+1, end);
        }
        else {
            for (int j=rightChildIndex+1; j<=end; j++) {
                if (preorder[j] <= root)
                    return false;
            }

            if (start+1 <= rightChildIndex-1)
                checkLeftSubtree = isPreorder(preorder, start+1, rightChildIndex - 1);
            if (rightChildIndex <= end)
                checkRightSubtree = isPreorder(preorder, rightChildIndex, end);
        }

        return checkLeftSubtree && checkRightSubtree;
    }

This approach is not O(1) space that since the calls on the call stack counts toward memory usage as well.

Actually we can improve the part where we make sure nodes beyond the right child are all bigger using recursion
as well.

.. code-block:: java

    public boolean verifyPreorder(int[] preorder) {
        if (preorder.length == 0)
            return true;

        return isPreorder(preorder, 0, preorder.length - 1,
                          Integer.MIN_VALUE, Integer.MAX_VALUE);
    }

    private boolean isPreorder(int[] preorder, int start, int end,
                               int min, int max) {
        if (start > end)
            return true;

        int root = preorder[start];

        if (root > max || root < min)
            return false;

        int rightChildIndex = start;

        while (rightChildIndex <= end && preorder[rightChildIndex] <= root) {
            rightChildIndex++;
        }

        return isPreorder(preorder, start+1, rightChildIndex-1, min, root) &&
                isPreorder(preorder, rightChildIndex, end, root, max);
    }

Here's an approach using a stack. ``low`` is the lower limit for future nodes. If we see any node smaller
thatn ``low`` then return ``false``

Smaller then top of stack, just push. When a bigger than top number is seen, pop until a larger number is found, and
update the new ``low``.

.. code-block:: java

    public boolean verifyPreorder(int[] preorder) {
        if (preorder.length == 0)
            return true;

        int low = Integer.MIN_VALUE;
        Stack<Integer> stk = new Stack<Integer>();

        for (int i=0; i<preorder.length; i++) {

            if (preorder[i] < low)
                return false;

            while (!stk.isEmpty() && preorder[i] > stk.peek()) {
                low = stk.pop();
            }

            stk.push(preorder[i]);
        }

        return true;
    }

Well this still take O(n) space. We can use the input array ``preorder`` for the stack and achieve
constant space.

.. code-block:: java

    public boolean verifyPreorder(int[] preorder) {

        int top=-1;
        int low = Integer.MIN_VALUE;

        for (int i=0; i<preorder.length; i++) {
            if (preorder[i] < low)
                return false;

            while (top > -1 && preorder[i] > preorder[top]) {
                low = preorder[top];
                top--;
            }

            // push
            preorder[++top] = preorder[i];
        }

        return true;
    }


