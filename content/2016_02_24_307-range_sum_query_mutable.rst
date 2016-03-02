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


Here is a version using an actual SegmentTreeNode. Notice how we still don't need to store the
low and high range that the node represents in the SegmentTreeNode class.

.. code-block:: java

    public class NumArray {
        class SegmentTreeNode {
            int sum;
            SegmentTreeNode left;
            SegmentTreeNode right;

            public SegmentTreeNode(int sum) {
                this.sum = sum;
            }
        }
        SegmentTreeNode root;
        int n = 0;

        public NumArray(int[] nums) {
            n = nums.length;
            if (n==0)
                return;
            root = buildSegmentTree(0, nums.length-1, nums);

        }

        private SegmentTreeNode buildSegmentTree(
                int low, int high, int[] nums) {

            if (low==high) {
                // leaf node
                return new SegmentTreeNode(nums[low]);
            }

            int middle = low + (high-low) / 2;

            SegmentTreeNode left = null;
            SegmentTreeNode right = null;


            if (middle >= low)
                left = buildSegmentTree(low, middle, nums);

            if (high>=middle+1)
                right = buildSegmentTree(middle+1, high, nums);

            SegmentTreeNode me = new SegmentTreeNode(left.sum + right.sum);
            me.left = left;
            me.right = right;

            return me;
        }

        void update(int i, int val) {
            updateHelper(root, 0, n-1, i, val);
        }

        private void updateHelper(SegmentTreeNode node, int low, int high,
                int index, int val) {

            if (low > high)
                return;

            if (low==high) {
                node.sum = val;
                return;
            }

            int middle = low + (high-low)/2;

            if (index >= low && index <= middle) {
                updateHelper(node.left, low, middle, index, val);
            }

            if (index > middle && index <= high) {
                updateHelper(node.right, middle+1, high, index, val);
            }

            node.sum = node.left.sum + node.right.sum;
        }

        public int sumRange(int i, int j) {
            return sumRangeHelper(0, n-1, root, i, j);
        }

        private int sumRangeHelper(int nLow, int nHigh,
                SegmentTreeNode node, int l, int h) {

            if (h < nLow || l > nHigh)
                return 0;

            if (nLow >=l && nHigh <=h)
                return node.sum;

            int middle = nLow + (nHigh-nLow)/2;

            return sumRangeHelper(nLow, middle, node.left, l, h) +
                    sumRangeHelper(middle + 1, nHigh, node.right, l, h);
        }
    }


