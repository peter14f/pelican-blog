096-unique_binary_search_trees
##############################

:date: 2015-11-19 12:44
:tags: Binary Search Trees, Dynamic Programming
:category: LeetCode
:slug: 096-unique_binary_search_trees

`LeetCode Problem Link <https://leetcode.com/problems/unique-binary-search-trees/>`_

The number of unique BSTs actually is a function of the number of unique items to be stored (items that can be
ordered)
How many unique BSTs can be formed with 0 items? Only one - the empty BST.
How many unique BSTs can be formed using 1 item? Only one. The item is stored at the root.
How many unique BSTs can be formed using 2 items? Well there can be two different roots.
For each number root, we need to calculate the number of different left subBSTs can be formed and the number of
different right subBSTs that can be formed.

.. code-block:: java

    public int numTrees(int n) {
        if (n < 0)
            throw new IllegalArgumentException("n must be a non-negative integer");
        else if (n==0)
            return 1;

        int[] numTreesWithNodes = new int[n+1];
        numTreesWithNodes[0] = 1;
        numTreesWithNodes[1] = 1;

        for (int i=2; i<=n; i++) {
            int cnt = 0;

            for (int root=1; root<=i; root++) {

                // number of nodes smaller than root
                int numSmaller = root - 1;
                int numLeftSubBSTs = numTreesWithNodes[numSmaller];

                // number of nodes bigger than root
                int numBigger = i - root;
                int numRightSubBSTs = numTreesWithNodes[numBigger];
                cnt += numRightSubBSTs * numLeftSubBSTs;
            }

            numTreesWithNodes[i] = cnt;
        }

        return numTreesWithNodes[n];
    }