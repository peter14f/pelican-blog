332-reconstruct_itinerary
#########################

:date: 2016-2-28 21:30
:tags: Graph, Directed Graph
:category: LeetCode
:slug: 332-reconstruct_itinerary

`LeetCode Problem Link <https://leetcode.com/problems/reconstruct-itinerary/>`_


Let's say currently you have ``n`` total choices as your next destination.

What we need to make sure is that when trying out ``ith`` solution, the recursive function
sees all other ``n-1`` choices.

Also ``x`` total tickets should result in an answer of size ``x+1``.

.. code-block:: java

    public List<String> findItinerary(String[][] tickets) {

        int n = tickets.length;
        List<String> ans = new ArrayList<String>();

        Map<String, List<String>> graph = new HashMap<String, List<String>>();

        for (int i=0; i<n; i++) {

            String from = tickets[i][0];
            String to = tickets[i][1];

            if (!graph.containsKey(from))
                graph.put(from, new ArrayList<String>());

            graph.get(from).add(to);

        }

        for (List<String> neighbors: graph.values()) {
            Collections.sort(neighbors);
        }

        if (graph.containsKey("JFK"))
            findItinerary(graph, ans, "JFK", n);

        return ans;
    }

    private boolean findItinerary(Map<String, List<String>> graph,
            List<String> ans, String cur, int n) {

        ans.add(cur);

        if (ans.size() == n+1) {
            return true;
        }

        if (graph.containsKey(cur)) {
            int origSize = graph.get(cur).size();

            for (int i=0; i<origSize; i++) {
                String next = graph.get(cur).remove(i);

                List<String> tmp = null;
                boolean removed = false;
                if (graph.get(cur).isEmpty()) {
                    tmp = graph.remove(cur);
                    removed = true;
                }

                // the recursive call will not see the ith choice
                boolean done = findItinerary(graph, ans, next, n);

                if (done) {
                    return true;
                }

                if (removed)
                    graph.put(cur, tmp);

                graph.get(cur).add(i, next);
            }
        }

        // hit a dead end, backtrack
        ans.remove(ans.size()-1);
        return false;
    }
