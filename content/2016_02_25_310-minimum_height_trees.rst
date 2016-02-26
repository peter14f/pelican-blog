310-minimum_height_trees
########################

:date: 2016-2-25 11:57
:tags:
:category: LeetCode
:slug: 310-minimum_height_trees

`LeetCode Problem Link <https://leetcode.com/problems/minimum-height-trees/>`_

``n`` nodes labeled from ``0`` to ``n-1``.

We need to build an undirected graph. Nodes with only one edge are leaf nodes. Nodes with more than one
edge are internal nodes. The root of the minumum height tree cannot possibly be a leaf node.

I go through each internal nodes and try to get the height of the tree using that node as the root.

But I got TLE for large TC.

What we can do it keep removing leaf nodes from the current graph until it's got < 2 nodes left.

.. code-block:: java

    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        List<Set<Integer>> graph = new ArrayList<Set<Integer>>();
        List<Integer> roots = new ArrayList<Integer>();

        if (n==1) {
            roots.add(0);
            return roots;
        }

        for (int i=0; i<n; i++) {
            graph.add(new HashSet<Integer>());
        }

        for (int i=0; i<edges.length; i++) {
            int a = edges[i][0];
            int b = edges[i][1];

            graph.get(a).add(b);
            graph.get(b).add(a);
        }

        List<Integer> leaves = new ArrayList<Integer>();

        for (int i=0; i<n; i++) {
            if (graph.get(i).size() == 1)
                leaves.add(i);
        }

        while (n > 2) {
            n = n - leaves.size();

            int numLeaves = leaves.size();

            for (int i=0; i<numLeaves; i++) {
                int leaf = leaves.remove(0);

                for (int neighbor: graph.get(leaf)) {
                    graph.get(neighbor).remove(leaf);

                    if (graph.get(neighbor).size() == 1) {
                        leaves.add(neighbor);
                    }
                }
            }
        }

        return leaves;
    }

