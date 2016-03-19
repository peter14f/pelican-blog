a04-shortest_distance_undirected_unweighted
###########################################

:date: 2016-3-19 14:33
:tags: Undirected Graph, BFS
:category:
:slug: a04-shortest_distance_undirected_unweighted

::

  Given a graph and two nodes src and dest, find the shortest distance and the shortest path from
  src to dest


.. code-block:: java

    // this is a undirected and unweighted graph
    public String shortestPathUnweighted(int n, int[][] edges, int src, int dest) {

        List<Set<Integer>> graph = new ArrayList<Set<Integer>>();
        for (int i=0; i<n; i++) {
            graph.add(new HashSet<Integer>());
        }

        int k = edges.length;
        for (int i=0; i<k; i++) {
            // a - b
            int a = edges[i][0];
            int b = edges[i][1];

            graph.get(a).add(b);
            graph.get(b).add(a);
        }

        Queue<Integer> q = new LinkedList<Integer>();
        HashSet<Integer> visited = new HashSet<Integer>();
        HashMap<Integer, Integer> prev = new HashMap<Integer, Integer>();

        visited.add(src);
        q.offer(src);

        int level = 0;

        while (!q.isEmpty()) {
            int size = q.size();

            for (int i=0; i<size; i++) {
                Integer node = q.poll();

                if (node == dest) {
                    StringBuffer sb = new StringBuffer();

                    while (node != src) {
                        sb.append(node);
                        sb.append(" ");
                        node = prev.get(node);
                    }

                    sb.append(node);
                    sb.reverse();
                    System.out.println("shortest distance from " + src + " " +
                                       dest + " is " + level);
                    return sb.toString();
                }

                Set<Integer> neighbors = graph.get(node);

                for (int neighbor : neighbors) {
                    if (!visited.contains(neighbor)) {
                        prev.put(neighbor, node);
                        visited.add(neighbor);
                        q.offer(neighbor);
                    }
                }
            }

            level++;
        }

        return "";
    }


