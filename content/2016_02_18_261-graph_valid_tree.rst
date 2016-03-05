261-graph_valid_tree
####################

:date: 2016-2-18 21:37
:tags: Graph, Undirected Graph, BFS, DFS, Check If Graph A Valid Binary Tree
:category: LeetCode
:slug: 261-graph_valid_tree

`LeetCode Problem Link <https://leetcode.com/problems/graph-valid-tree/>`_

::

    Given ``n`` nodes labeled from ``0`` to ``n - 1`` and a list of
    undirected edges (each edge is a pair of nodes), write a function to
    check whether these edges make up a valid tree.

    For example:

    Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.

    Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.

    Hint:

    Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], what should your return? Is this case a valid tree?

    According to the definition of tree on Wikipedia:
    “a tree is an undirected graph in which any two vertices are connected by exactly one path.
    In other words, any connected graph without simple cycles is a tree.”

    Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Please note that this problem is checking for any tree, not just binary trees. So the parent node
may have any number of children, not simply just 2.

We must check two things. First, a cycle does not exist in the undirected graph.
We've written similar clone in 133-clone_graph.

Second, start with any node in the graph, you should be able to reach all other nodes. If a node is
not reachable, that would imply that the tree has two roots.


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

    (A,B) (B,D) (A,C), (D,C)

              A
             / \
             B  C
            /   |
           D-----


If you draw this graph out as a directed graph, you won't be able to detect a cycle on it because C
is the only sink node.


Revisit (03/02/2016)

Here is the code I got using BFS this time. I like how I simplified the data structure I'm using for the graph.
But I got so concerned with not going back to the previous node, I ended storing (cur, prev) in  a HashMap. There
is actually no need for that. We can rely on ``visited``. Just do not go back to node already **visited**. That's
try again.

.. code-block:: java

    public boolean validTree(int n, int[][] edges) {

        int k = edges.length;

        if (k==0) {
            if (n==0 || n==1) {
                // empty tree or the root by itself
                return true;
            }
            else {
                // 2+ nodes and no edges
                return false;
            }
        }

        List<Set<Integer>> graph = new ArrayList<Set<Integer>>();

        for (int i=0; i<n; i++) {
            graph.add(new HashSet<Integer>());
        }

        for (int i=0; i<k; i++) {
            // a -- b
            int a = edges[i][0];
            int b = edges[i][1];

            graph.get(a).add(b);
            graph.get(b).add(a);
        }

        boolean cycleFound = false;

        Queue<Integer> q = new LinkedList<Integer>();
        q.add(edges[0][0]);

        HashSet<Integer> visited = new HashSet<Integer>();
        HashMap<Integer, Integer> cameFrom = new HashMap<Integer, Integer>();

        while (!q.isEmpty()) {
            int cur = q.poll();

            if (visited.contains(cur)) {
                cycleFound = true;
                break;
            }

            Set<Integer> neighbors = graph.get(cur);

            for (int neighbor : neighbors) {
                // do not go back to the node that you just came from

                if (cameFrom.containsKey(cur) && cameFrom.get(cur) == neighbor) {
                    // was just at this neighbor, that's how we got to cur
                    continue;
                }

                q.offer(neighbor);
                cameFrom.put(neighbor, cur);
            }

            visited.add(cur);
        }

        if (cycleFound)
            return false;

        return visited.size() == n;
    }

Finally, here what I'd say is the perfect BFS solution for this problem.

.. code-block:: java

    public boolean validTree(int n, int[][] edges) {

        List<Set<Integer>> graph = new ArrayList<Set<Integer>>();

        for (int i=0; i<n; i++) {
            graph.add(new HashSet<Integer>());
        }

        int k=edges.length;

        if (k==0) {
            // no edges
            if (n==0 || n==1)
                return true;
            else
                return false;
        }

        for (int i=0; i<k; i++) {
            int a = edges[i][0];
            int b = edges[i][1];

            graph.get(a).add(b);
            graph.get(b).add(a);
        }

        boolean cycle = false;

        // could start anywhere
        Queue<Integer> q = new LinkedList<Integer>();
        HashSet<Integer> visited = new HashSet<Integer>();

        q.add(edges[0][0]);

        while (!q.isEmpty()) {
            int cur = q.poll();

            if (visited.contains(cur)) {
                cycle = true;
                break;
            }

            Set<Integer> neighbors = graph.get(cur);

            for (int neighbor: neighbors) {
                // neighbor already in visited set
                if (visited.contains(neighbor))
                    continue;

                q.offer(neighbor);
            }

            visited.add(cur);
        }

        if (cycle)
            return false;

        // all nodes reachable?
        return visited.size() == n;
    }

I would like to point out that the graph given in 133-clone_graph is actually not truly undirected because
it does not contain both edges ``(a, b)`` and ``(b, a)`` when two nodes a and b are connected.

A good exercise to do next would be the dijkstra's algorithm. Dijkstra should work for weighted directed and
undirected graphs to find out the shortest distance to all other nodes from a src node. I've noticed that all
the graph problems on LeetCode are unweighted graphs.

