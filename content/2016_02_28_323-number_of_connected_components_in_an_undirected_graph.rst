323-number_of_connected_components_in_an_undirected_graph
#########################################################

:date: 2016-2-28 0:38
:tags: Undirected Graph
:category: LeetCode
:slug: 323-number_of_connected_components_in_an_undirected_graph

`LeetCode Problem Link <https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/>`_

Given ``n`` nodes labeled from ``0`` to ``n-1`` and a list of undirected edges.

Find the number of connected components in this undirected graph.

This problem would more of what I typically imagine a blob analysis problem would be if we were
given dots in a 2D grid.

But this is clearly a union-find problem. My question is, is it even necessary for me to build the
graph in a List<Set<Integer>> data structure?

My guess is not! Simply traversing all the edges in the graph is good enough.

This is as typical as an union-find problem can get!

.. code-block:: java

    class UnionFind {
        int[] parent; // parent[i] is the parent of i
        int size;

        public UnionFind(int n) {
            parent = new int[n];

            for (int i=0; i<n; i++)
                parent[i] = i;

            size = n;
        }

        public void union(int a, int b) {
            while (a != parent[a]) {
                a = parent[a];
            }

            while (b != parent[b]) {
                b = parent[b];
            }

            int minBlob = Math.max(a, b);
            parent[a] = minBlob;
            parent[b] = minBlob;

            if (a != b) {
                size--;
            }
        }

        public int getSize() {
            return size;
        }
    }

    public int countComponents(int n, int[][] edges) {

        UnionFind uf = new UnionFind(n);

        for (int i=0; i<edges.length; i++) {
            // a -- b
            int a = edges[i][0];
            int b = edges[i][1];

            uf.union(a, b);
        }

        return uf.getSize();
    }

