095-unique_binary_search_tree_ii
################################

:date: 2015-11-19 21:30
:tags: Binary Search Trees, Recursion, Dynamic Programming, Cloning Trees
:category: LeetCode
:slug: 095-unique_binary_search_tree_ii

`LeetCode Problem Link <https://leetcode.com/problems/unique-binary-search-trees-ii/>`_

The problem is similar to 096-unique_binary_search_trees in that we must get the solution to ``n`` from the
solution to ``n-1``. The tricky part is that we cannot just simply clone the BSTs. We must provide a mapping.

What do I mean by this? The BST with one node we find the ArrayList will be the node containing the value ``1``. But
in the case of having a total of two nodes and when the root is ``1``, the right subBST must be the node containing
the value ``2`` instead of the value ``1``.

.. code-block:: java

    public List<TreeNode> generateTrees(int n) {

        List<TreeNode> empty = new ArrayList<TreeNode>();
        if (n==0)
            return empty;

        empty.add(null);

        List<List<TreeNode>> bstNodes = new ArrayList<List<TreeNode>>();


        bstNodes.add(empty); // 0 nodes

        for (int numNodes=1; numNodes<=n; numNodes++) {
            List<TreeNode> cur = new ArrayList<TreeNode>();

            for (int r=1; r<=numNodes; r++) {


                int numLeftSubBSTNodes = r - 1;
                List<TreeNode> leftSubBSTs = bstNodes.get(numLeftSubBSTNodes);
                int numRightSubBSTNodes = numNodes - r;
                List<TreeNode> rightSubBSTs = bstNodes.get(numRightSubBSTNodes);

                for (TreeNode bst1: leftSubBSTs) {
                    for (TreeNode bst2: rightSubBSTs) {
                        TreeNode root = new TreeNode(r);
                        TreeNode cloneLeft = cloneTree(bst1, numLeftSubBSTNodes, 1, r-1, r);
                        TreeNode cloneRight = cloneTree(bst2, numRightSubBSTNodes, r+1, numNodes, r);
                        root.left = cloneLeft;
                        root.right = cloneRight;
                        cur.add(root);
                    }
                }
            }

            bstNodes.add(cur);
        }

        return bstNodes.get(n);
    }

    private TreeNode cloneTree(TreeNode bst, HashMap<Integer, Integer> map) {
        if (bst==null)
            return null;

        TreeNode cur = new TreeNode(map.get(bst.val));
        cur.left = cloneTree(bst.left, map);
        cur.right = cloneTree(bst.right, map);

        return cur;
    }

    private TreeNode cloneTree(TreeNode bst, int num, int low, int high, int root) {
        if (bst==null)
            return null;

        // old tree contains 1 through num,
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();

        int j=low;

        for (int i=1; i<=num; i++) {
            if (j==root)
                j++;

            map.put(i, j);
            j++;
        }

        return cloneTree(bst, map);
    }


The recursive solution turns out to be way cleaner.

.. code-block:: java

    public List<TreeNode> generateTrees(int n) {

        if (n==0)
            return new ArrayList<TreeNode>();

        return generateTrees(1, n);
    }

    public List<TreeNode> generateTrees(int start, int end) {

        List<TreeNode> bsts = new ArrayList<TreeNode>();

        if (start > end) {
            bsts.add(null);
        }

        for (int r=start; r<=end; r++) {

            List<TreeNode> lefts = generateTrees(start, r-1);
            List<TreeNode> rights = generateTrees(r+1, end);

            for (TreeNode left: lefts) {
                for (TreeNode right: rights) {
                    TreeNode root = new TreeNode(r);
                    root.left = left;
                    root.right = right;
                    bsts.add(root);
                }
            }

        }

        return bsts;
    }