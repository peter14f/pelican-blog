333-largest_bst_subtree
#######################

:date: 2016-2-28 21:31
:tags: Binary Search Trees, Binary Trees
:category: LeetCode
:slug: 333-largest_bst_subtree

`LeetCode Problem Link <https://leetcode.com/problems/largest-bst-subtree/>`_

Given a binary tree, return the size of the largest BST subtree you can find.

.. code-block:: java

    // size of the current tree
    // range of the nodes in current tree
    class Result {
        int size;
        int lower;
        int upper;

        public Result(int s, int l, int u) {
            size = s;
            lower = l;
            upper = u;
        }

        public String toString() {
            return "size=" + size + " low=" + lower + " high=" + upper;
        }
    }

    public int largestBSTSubtree(TreeNode root) {
        int[] maxSize = {0};
        traverse(root, maxSize);
        return maxSize[0];
    }

    // return a Result of -1 means subtree whose root is cur cannot be a BST
    //
    //
    private Result traverse(TreeNode cur, int[] maxSize) {

        if (cur == null) {
            // no nodes
            return new Result(0, Integer.MAX_VALUE, Integer.MIN_VALUE);
        }

        Result left = traverse(cur.left, maxSize);
        Result right = traverse(cur.right, maxSize);

        if (left.size == -1 || right.size == -1 ||
                cur.val <= left.upper || cur.val >= right.lower) {
            return new Result(-1, 0, 0);
        }

        int size = 1 + left.size + right.size;

        if (size > maxSize[0]) {
            maxSize[0] = size;
        }

        // left subtree is a bst
        // right subtree is a bst
        //

        Result r = new Result(size, Math.min(left.lower, cur.val), Math.max(cur.val, right.upper));
        System.out.println(r);

        return r;
    }

Returning (-1, MAX, MIN) means not a BST an no numbers can be in the range (MAX, MIN)

Returning (1, a, a) means the leaf node of value ``a`` is a BST.

Returning (2, a, b) means the it's a BST of size 2 and the smallest value in the bst is ``a`` and
the biggest value in the bst is ``b``.

