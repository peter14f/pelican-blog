210-course_scheduel_ii
######################

:date: 2016-1-27 18:27
:tags: Directed Graph, Topological Ordering, BFS, DFS
:category: LeetCode
:slug: 210-course_scheduel_ii

`LeetCode Problem Link <https://leetcode.com/problems/course-schedule-ii/>`_

I will show the BFS solution first. Like in 207-course_scheulde, we start with **source nodes**, nodes whose
in-degree is zero. We insert them into a queue. The source nodes should be the classes to take last because it has
prerequisites but no other classes depend on it. As we take out nodes from the queue, we assign the node in the right
spot in the array at the tail. Then we remove edges coming from the node and update the in-degrees of the affected
nodes.

If the total number of nodes retrieved from the queue does not match with the total number of nodes in the graph, then
there exists a cycle.

.. code-block:: java

    public int[] findOrder(int numCourses, int[][] prerequisites) {
        HashMap<Integer, HashSet<Integer>> graph = new HashMap<Integer, HashSet<Integer>>();
        int[] order = new int[numCourses];
        int[] inDegree = new int[numCourses];

        // build the graph first
        for (int i=0; i<prerequisites.length; i++) {
            int course = prerequisites[i][0];
            int dependOn = prerequisites[i][1];

            if (graph.containsKey(course)) {
                graph.get(course).add(dependOn);
            }
            else {
                HashSet<Integer> dependsOn = new HashSet<Integer>();
                dependsOn.add(dependOn);
                graph.put(course, dependsOn);
            }
        }

        for (HashSet<Integer> courses: graph.values()) {
            for (int course: courses) {
                inDegree[course]++;
            }
        }

        Queue<Integer> q = new LinkedList<Integer>();

        for (int i=0; i<numCourses; i++) {
            if (inDegree[i] == 0) {
                // source node
                q.offer(i);
            }
        }

        int index = numCourses-1;
        int nodeInserted = 0;

        while (!q.isEmpty()) {
            int curSourceNode = q.poll();
            nodeInserted++;

            order[index] = curSourceNode;
            index--;

            if (graph.containsKey(curSourceNode)) {
                HashSet<Integer> neighbors = graph.get(curSourceNode);

                for (int course: neighbors) {
                    inDegree[course]--;
                    if (inDegree[course] == 0) {
                        q.add(course);
                    }
                }
            }
        }

        if (nodeInserted < numCourses)
            return new int[0];

        return order;
    }

Here is the DFS solution. The **sink node** (last traversed with DFS when the call stack contains the most recursive
calls) will be placed at the beginning of the order. Note that our ``dfs()`` method still returns if a cycle has
been found.

.. code-block:: java

    public int[] findOrder(int numCourses, int[][] prerequisites) {

        HashMap<Integer, HashSet<Integer>> graph = new HashMap<Integer, HashSet<Integer>>();

        for (int i=0; i<prerequisites.length; i++) {
            int course = prerequisites[i][0];
            int dependsOn = prerequisites[i][1];

            if (graph.containsKey(course)) {
                graph.get(course).add(dependsOn);
            }
            else {
                HashSet<Integer> courses = new HashSet<Integer>();
                courses.add(dependsOn);
                graph.put(course, courses);
            }
        }

        int[] states = new int[numCourses];
        int[] order = new int[numCourses];
        int[] index = {0};

        boolean cycleFound = false;

        for (int i=0; i<numCourses; i++) {
            if (states[i] == 0) {
                if (dfs(graph, i, index, states, order)) {
                    cycleFound = true;
                    break;
                }
            }
        }

        if (cycleFound)
            return new int[0];
        else
            return order;
    }

    // returns if a cycle is detected
    private boolean dfs(HashMap<Integer, HashSet<Integer>> graph,
            int node,
            int[] index,
            int[] states,
            int[] order
            ) {

        states[node] = 1;

        if (graph.containsKey(node)) {
            HashSet<Integer> neighbors = graph.get(node);

            for (int neighbor: neighbors) {
                if (states[neighbor] == 1)
                    return true;
                else if (states[neighbor] == 0) {
                    if (dfs(graph, neighbor, index, states, order)) {
                        return true;
                    }
                }
            }
        }

        states[node] = 2;
        order[index[0]] = node;
        index[0]++;

        return false;
    }
