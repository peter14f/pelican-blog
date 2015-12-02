124-binary_tree_maximum_path_sum
################################

:date: 2015-12-1 21:02
:tags: Recursion, Binary Trees
:category: LeetCode
:slug: 124-binary_tree_maximum_path_sum

`LeetCode Problem Link <https://leetcode.com/problems/binary-tree-maximum-path-sum/>`_

For this problem, a path must contain at least one node in the binary tree unless the

I want to do DFS, but we are missing the parent link. One way we could solve this problem is build a HashMap to find
the parent of a node and then perform DFS from each and every node. But this takes exponential time and will not pass
the large test case on OJ.

.. code-block:: java

    public int maxPathSum(TreeNode root) {
        if (root==null)
            return 0;

        if (root.left == null && root.right == null) {
            return root.val;
        }

        HashMap<TreeNode, TreeNode> parents = new HashMap<TreeNode, TreeNode>();
        buildParentMap(root, null, parents);
        List<TreeNode> nodes = new ArrayList<TreeNode>();
        nodes.add(root);

        for (TreeNode n: parents.keySet()) {
            nodes.add(n);
        }

        int[] maxSum = {0};

        for (TreeNode n: nodes) {
            HashSet<TreeNode> visited = new HashSet<TreeNode>();
            dfs(n, visited, 0, maxSum, parents);
        }

        return maxSum[0];
    }

Here is another approach that does not require starting the dfs from every node. The method ``maxPathSum`` that takes
two arguments returns the maximum path sum including the ``node`` node that can be extended. So which paths can
contain the ``node`` and can be extended?

  1. path containing the node only
  2. path containing the node and the max path containing its left child node
  3. path containing the node and the max path containing its right child node

Tha maximum of the above three values will be returned by ``maxPathSum``.

Note that the path containing the node **plus** the max path containing its left child node **plus** the max path
containing its right child node **CANNOT** be further expanded. So this is why we also pass in an int[] ``max`` into
``maxPathSum``. We still calculate the sum for this path and if it exceeds ``max[0]``, ``max[0]`` will be overwritten.
We just don't return the this value.

Since the of a path for this problem must contain at this one node. We initialize ``max[0]`` to ``root.val``.
Each node in the binary tree is visited once so this takes O(n) time. The space complexity is O(n) which is number of
function calls on the stack in the worst case. 

.. code-block:: java

    public int maxPathSum(TreeNode root) {

        if (root==null)
            return 0;

        // the path must contain one node at least
        int[] max = {root.val};

        int me = maxPathSum(root, max);

        return max[0];
    }

    private int maxPathSum(TreeNode node, int[] max) {

        if (node.left == null && node.right == null) {
            if (node.val > max[0])
                max[0] = node.val;

            return node.val;
        }

        int leftMax = Integer.MIN_VALUE;
        int rightMax = Integer.MIN_VALUE;

        if (node.left != null) {
            leftMax = maxPathSum(node.left, max);
        }

        if (node.right != null) {
            rightMax = maxPathSum(node.right, max);
        }

        int selfOnly = node.val;

        int plusLeft = node.val + leftMax;
        if (leftMax < 0 && node.val < 0 && plusLeft > 0)
            plusLeft = Integer.MIN_VALUE;

        int plusRight = node.val + rightMax;
        if (rightMax < 0 && node.val < 0 && plusRight > 0)
            plusRight = Integer.MIN_VALUE;

        int includeNode = Math.max(selfOnly, Math.max(plusLeft, plusRight));
        if (includeNode > max[0]) {
            max[0] = includeNode;
        }

        int cannotExtend = plusLeft + rightMax;
        if (plusLeft < 0 && rightMax < 0 && cannotExtend > 0)
            cannotExtend = Integer.MIN_VALUE;

        if (cannotExtend > max[0])
            max[0] = cannotExtend;

        return includeNode;
    }


