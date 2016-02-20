269-alien_dictionary
####################

:date: 2016-2-19 14:09
:tags: Topological Sorting, Directed Graph
:category: LeetCode
:slug: 269-alien_dictionary

`LeetCode Problem Link <https://leetcode.com/problems/alien-dictionary/>`_

First, we have to understand that the input array is sorted, not the word itself.

Just like in English a sorted word list could be

["air", "baseball", "cat"]

but "air" is not a sorted string.
    "baseball" is not a sorted string.
    "cat" is not a sorted string.

I've seen some solutions online assuming that each word is sorted. They are solving a different problem.

In the given example, the sorted input array is

 [
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

We should build the graph "w->e->r->t->f".

Once the graph is built, we just need to run topological sort on the directed graph.

Let's review how to run topological sort again using DFS.
Each node in the beginning has a state of ``0``.

Your DFS method should return a boolean value (``true`` if cycle is detected).

Loop through the nodes and start DFS if node has a state of zero.

First thing inside the DFS method is to set the node state to ``1``.

Loop through the nodes neighbors, if neighbor's state is ``1`` a cycle is found.

If neighbor's state is ``2``, don't call DFS on it.
Else if neighbor's state is ``0``, recursively call DFS on it.

Set node's state to ``2``.

.. code-block:: java

    public String alienOrder(String[] words) {

        HashMap<Character, Set<Character>> graph = new HashMap<Character, Set<Character>>();

        String prev = null;

        for (String word: words) {

            if (word.length() == 0)
                continue;

            for (int i=0; i<word.length(); i++) {
                char c = word.charAt(i);
                if (!graph.containsKey(c)) {
                    graph.put(c, new HashSet<Character>());
                }
            }

            if (prev != null && !prev.equals(word)) {
                addToGraph(prev, word, graph);
            }

            prev = word;
        }

        //System.out.println(graph);

        StringBuffer sb = new StringBuffer();

        HashMap<Character, Integer> states = new HashMap<Character, Integer>();
        for (char c: graph.keySet()) {
            states.put(c, 0);
        }

        for (char c: states.keySet()) {
            if (states.get(c) == 0) {
                if (dfsTopologicalSort(graph, c, states, sb)) {
                    return "";
                }
            }
        }

        return sb.reverse().toString();
    }

    private boolean dfsTopologicalSort(
            HashMap<Character, Set<Character>> graph,
            char c,
            HashMap<Character, Integer> states,
            StringBuffer sb) {

        boolean foundCycle = false;

        // set state to one
        states.put(c, 1);

        for (Character neighbor: graph.get(c)) {

            if (states.get(neighbor) == 1) {
                return true;
            }
            else if (states.get(neighbor) == 0) {
                foundCycle = dfsTopologicalSort(graph, neighbor, states, sb);
                if (foundCycle)
                    return true;
            }

        }

        states.put(c, 2);
        sb.append(c);

        return false;
    }

    private void addToGraph(String prev, String cur, HashMap<Character, Set<Character>> graph) {

        int length = Math.min(prev.length(), cur.length());

        for (int i=0; i<length; i++) {
            char p = prev.charAt(i);
            char q = cur.charAt(i);

            // relationship can only be seen on the first pair different characters
            if (p != q) {

                // p -> q (p bigger than q)

                if (!graph.containsKey(p)) {
                    HashSet<Character> neighbors = new HashSet<Character>();
                    neighbors.add(q);
                    graph.put(p, neighbors);
                }
                else {
                    graph.get(p).add(q);
                }

                if (!graph.containsKey(q)) {
                    HashSet<Character> neighbors = new HashSet<Character>();
                    graph.put(q, neighbors);
                }

                break;
            }
        }
    }

Here is the same problem solved using BFS topological sort.

.. code-block:: java

    public String alienOrder(String[] words) {
        HashMap<Character, Set<Character>> graph = new HashMap<Character, Set<Character>>();
        HashMap<Character, Integer> indegrees = new HashMap<Character, Integer>();
        String prev = null;

        for (String word: words) {
            if (word.length() == 0)
                continue;

            for (int i=0; i<word.length(); i++) {
                char c = word.charAt(i);

                if (!graph.containsKey(c)) {
                    HashSet<Character> neighbors = new HashSet<Character>();
                    graph.put(c, neighbors);
                }

                if (!indegrees.containsKey(c)) {
                    indegrees.put(c, 0);
                }
            }

            if (prev != null && !word.equals(prev)) {
                addToGraph(graph, indegrees, prev, word);
            }

            prev = word;
        }

        //System.out.println(graph);

        Queue<Character> q = new LinkedList<Character>();

        for (Character c: indegrees.keySet()) {
            if (indegrees.get(c) == 0) {
                q.offer(c);
            }
        }

        StringBuffer sb = new StringBuffer();

        while (!q.isEmpty()) {
            char c = q.poll();

            sb.append(c);

            for (char neighbor: graph.get(c)) {
                indegrees.put(neighbor, indegrees.get(neighbor) - 1);
                if ((indegrees.get(neighbor) == 0)) {
                    q.offer(neighbor);
                }
            }

            graph.remove(c);
        }

        // this means there exists a cycle:
        // there should a source node until the graph is empty
        //
        if (!graph.isEmpty()) {
            return "";
        }

        // indegree being zero is actually the source node
        // so no need to reverse
        return sb.toString();
    }

    private void addToGraph(HashMap<Character, Set<Character>> graph,
                            HashMap<Character, Integer> indegrees,
                            String prev,
                            String cur) {

        int min = Math.min(prev.length(), cur.length());

        for (int i=0; i<min; i++) {
            char p = prev.charAt(i);
            char q = cur.charAt(i);

            // p -> q
            if (p != q) {
                if (!graph.get(p).contains(q)) {
                    graph.get(p).add(q);
                    indegrees.put(q, indegrees.get(q)+1);
                }
                break;
            }
        }
    }

