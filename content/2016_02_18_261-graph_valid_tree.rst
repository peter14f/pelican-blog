261-graph_valid_tree
####################

:date: 2016-2-18 21:37
:tags: Graph, Undirected Graphs, BFS, DFS, Check If Graph A Valid Binary Tree
:category: LeetCode
:slug: 261-graph_valid_tree

`LeetCode Problem Link <https://leetcode.com/problems/graph-valid-tree/>`_

Build the graph first. Here is how I'm doing the check.
I am building the graph such that the edge connecting two nodes are bi-directional.

Start BFS from node 0, make sure that
1) no cycle is found
2) at the end of the search, all nodes are reached

What would happen when you do BFS and there is a cycle? A particular node will be put on the queue
twice! So be sure to check the visited status as soon as a node is taken out from the queue.

If both conditions are met, then the graph is a valid tree.

.. code-block:: java

    class Node {
        int val;
        List<Integer> neighbors;
        public Node(int x) {
            val = x;
            neighbors = new ArrayList<Integer>();
        }
    }

    public boolean validTree(int n, int[][] edges) {
        int k = edges.length;

        if (n==0 && k==0)
            return true;

        Node[] nodes = new Node[n];

        for (int i=0; i<n; i++) {
            nodes[i] = new Node(i);
        }

        for (int i=0; i<k; i++) {
            nodes[edges[i][0]].neighbors.add(edges[i][1]);
            nodes[edges[i][1]].neighbors.add(edges[i][0]);
        }

        boolean[] visited = new boolean[n];

        Queue<Integer> q = new LinkedList<Integer>();
        q.offer(0);

        while (!q.isEmpty()) {
            int nodeId = q.poll();

            if (visited[nodeId])
                return false;

            for (int neighbor: nodes[nodeId].neighbors) {
                if (!visited[neighbor]) {
                    q.offer(neighbor);
                }
            }

            visited[nodeId] = true;
        }

        for (int i=0; i<n; i++) {
            if (!visited[i])
                return false;
        }

        return true;
    }

We could also do this problem using DFS.

.. code-block:: java

    class Node {
        int val;
        List<Integer> neighbors;

        public Node(int x) {
            val = x;
            neighbors = new ArrayList<Integer>();
        }
    }

    private boolean validTree(int n, int[][] edges) {

        Node[] nodes = new Node[n];
        for (int i=0; i<n; i++) {
            nodes[i] = new Node(i);
        }

        for (int i=0; i<edges.length; i++) {
            nodes[edges[i][0]].neighbors.add(edges[i][1]);
            nodes[edges[i][1]].neighbors.add(edges[i][0]);
        }

        boolean[] visited = new boolean[n];

        if (dfsFoundCycle(0, -1, visited, nodes)) {
            return false;
        }

        for (int i=0; i<n; i++) {
            if (!visited[i])
                return false;
        }

        return true;
    }

    private boolean dfsFoundCycle(int nodeId, int sourceId, boolean[] visited, Node[] nodes) {

        Node cur = nodes[nodeId];

        if (visited[nodeId])
            return true;

        visited[nodeId] = true;

        for (int neighbor : cur.neighbors) {
            if (neighbor == sourceId)
                continue;

            if (dfsFoundCycle(neighbor, nodeId, visited, nodes)) {
                return true;
            }
        }

        return false;
    }

Note: You might be wondering why for a binary tree, we should use a undirected graph. After all,
the parent should act like the source of the edge, and the child should act like the destination of
the edge. And we've done several problems detecting a cycle in a directed graph using DFS or BFS in
topological sort.

Here I am going to show a directed graph that has a cycle in a undirected graph and cannot be
a valid binary tree.

::

    (A,B) (B,C) (D,E)

              A
             / \
             B  C
            /   |
           D-----


If you draw this graph out as a directed graph, you won't be able to detect a cycle on it because C
is the only sink node.