307-range_sum_query_mutable
###########################

:date: 2016-2-24 17:05
:tags: Range Sum, Segment Tree, Full Binary Trees
:category: LeetCode
:slug: 307-range_sum_query_mutable

`LeetCode Problem Link <https://leetcode.com/problems/range-sum-query-mutable/>`_

Use a segment tree since the number of gets and updates are the same.

A segment tree is a *full* binary tree -> a binary tree where all nodes have either 0 or 2 children.

Something you might want to memorize regarding a full binary tree is that a full binary tree with ``n`` leaf nodes
has ``n-1`` internal nodes. Therefore, the total number of nodes will be ``2n-1``.

We are not using the ``0`` index and starting root node and index ``1``. So our array needs to be of size ``2n``.

But in practice ``2n`` is not always a power of two. We need to find a power of two that's bigger than ``2n`` call it
``x`` and then multiply it by ``2`` again.

This is a good problem to practice the array implementation of a segment tree. Almost all operations are recursive.
We need to always start at index 1 where the root is and specify the range that node represents. In the case where the
input int array has 5 elements, the range that the root segment tree node represents would be [0, 4].



.. code-block:: java

    public class NumArray {

        int[] segTree;
        int[] nums;

        public NumArray(int[] nums) {
            this.nums = nums;

            int n = nums.length;
            // n leaves -> n-1 internal nodes --> total # of nodes = 2n - 1
            // we need 2n slots at least since not using index 0
            // but 2n is not necessarily a power of 2 (we're using an array)
            // so find x who is a power of 2 and is bigger than 2n
            // multiply x by 2

            if (n==0)
                return;

            int x = 1;
            int size = 2 * n;
            while (x < size) {
                x = x << 1;
            }
            // an approximation that I find people often use if 4n
            segTree = new int[2*x];

            //System.out.println(segTree.length);

            fillInSegTree(1, 0, n-1);
        }

        // [start, end] is the range that this node represent
        private void fillInSegTree(int node, int start, int end) {

            if (start == end) {
                segTree[node] = nums[start];
                return;
            }

            int middle = start + (end-start) / 2;

            fillInSegTree(node*2, start, middle);
            fillInSegTree(node*2 + 1, middle + 1, end);

            segTree[node] = segTree[2*node] + segTree[2*node+1];
        }

        void update(int i, int val) {
            updateHelper(1, 0, nums.length-1, i, val);
        }

        // [start, end] is the range represented by node
        // need to find the leaf node and update its value
        private void updateHelper(int node, int start, int end, int index, int val) {

            if (start == end) {
                segTree[node] = val;
                return;
            }

            int middle = start + (end - start) / 2;

            if (index >= start && index <= middle) {
                updateHelper(node*2, start, middle, index, val);
            }
            else if (index > middle && index <= end) {
                updateHelper(node*2 + 1, middle+1, end, index, val);
            }
            else {
                // invalid index
                return;
            }

            segTree[node] = segTree[node*2] + segTree[node*2+1];
        }

        public int sumRange(int i, int j) {
            return sumRangeHelper(1, 0, nums.length-1, i, j);
        }

        // [start, end] is the range represented by node
        private int sumRangeHelper(int node, int start, int end, int rangeBegin, int rangeEnd) {

            if (end < rangeBegin || start > rangeEnd) {
                // range represented by node is outside of the query range
                return 0;
            }
            else if (start >= rangeBegin && end <= rangeEnd) {
                // range represented by node is completely inside of the query range
                return segTree[node];
            }

            int middle = start + (end - start)/2;

            int left = sumRangeHelper(node*2, start, middle, rangeBegin, rangeEnd);
            int right = sumRangeHelper(node*2 + 1, middle+1, end, rangeBegin, rangeEnd);

            return left + right;
        }
    }

