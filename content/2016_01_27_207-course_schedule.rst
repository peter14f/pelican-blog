207-course_schedule
###################

:date: 2016-1-27 11:42
:tags: Directed Graph, Detecting Cycles in Directed Graphs, BFS, DFS
:category: LeetCode
:slug: 207-course_schedule

`LeetCode Problem Link <https://leetcode.com/problems/course-schedule/>`_

For the DFS approach all we need to remember is that each vertex can be in 3 different states. The initial value ``0``
means the vertex has not been looked at yet. Value ``1``, searching, means that we are in the process of going through
all paths from this vertex. Value ``2``, visited, means that we've verified that all paths from this vertex do not
result in a cycle.

``hasCycle`` should only be called on a vertex when it's in state ``0``.

In the recursive call  ``hasCycle``, if we see a neighbor who's in state ``1`` then we know that a cycle has been
detected.

.. code-block:: java

    public boolean canFinish(int numCourses, int[][] prerequisites) {
        HashMap<Integer, HashSet<Integer>> graph = new HashMap<Integer, HashSet<Integer>>();

        for (int i=0; i<prerequisites.length; i++) {
            int course = prerequisites[i][0];
            int prereqCourse = prerequisites[i][1];

            if (graph.containsKey(course)) {
                graph.get(course).add(prereqCourse);
            }
            else {
                HashSet<Integer> prereqs = new HashSet<Integer>();
                prereqs.add(prereqCourse);
                graph.put(course, prereqs);
            }
        }

        /* 0 - new node that has not been looked at yet
         * 1 - checking, meaning that we're in the process of checking all paths from vertex
         * 2 - visited, meaning we've checked all paths from this vertex do not result in a cycle
         */
        int[] visited = new int[numCourses];


        for (int i=0; i<numCourses; i++) {

            if (visited[i] == 0) {
                if (hasCycle(graph, visited, i)) {
                    return false;
                }
            }
        }

        return true;
    }

    /* this helper method should be called only when
     * visited[node] is 0
     */
    private boolean hasCycle(HashMap<Integer, HashSet<Integer>> graph,
            int[] visited,
            int node) {

        visited[node] = 1;

        if (graph.containsKey(node)) {
            HashSet<Integer> neighbors = graph.get(node);

            for (int v: neighbors) {
                /*  ignore if state is 2
                 *  call hasCycle if state is 0
                 *  return false if state is 1
                 */
                if (visited[v] == 0) {
                    if (hasCycle(graph, visited, v))
                        return true;
                }
                else if (visited[v] == 1) {
                    return true;
                }
            }

        }

        visited[node] = 2;
        return false;
    }

Here is the BFS approach. Note that nodes that have in-degree of ``0`` are call source nodes. For a directed graph to
not have a cycle, it must have a **source node**.

We will use a queue to store the **source nodes** in the current graph, then we will take out each source node and the
edges from the source node. Update the in-degrees as edges are removed from the graph. Insert newly found source nodes
into the queue. At the end of this process, we should find that the number nodes taken out from the queue to be the
same as the number of nodes in the original graph. Otherwise, there exists a cycle.

.. code-block:: java

    public boolean canFinish(int numCourses, int[][] prerequisites) {

        HashMap<Integer, HashSet<Integer>> graph = new HashMap<Integer, HashSet<Integer>>();
        int[] inDegree = new int[numCourses];

        for (int i=0; i<prerequisites.length; i++) {
            int course = prerequisites[i][0];
            int prereqCourse = prerequisites[i][1];

            if (graph.containsKey(course)) {
                graph.get(course).add(prereqCourse);
            }
            else {
                HashSet<Integer> courses = new HashSet<Integer>();
                courses.add(prereqCourse);
                graph.put(course, courses);
            }
        }

        for (HashSet<Integer> courses: graph.values()) {
            for (int course: courses) {
                inDegree[course]++;
            }
        }

        // courses that do not have prerequisites
        Queue<Integer> q = new LinkedList<Integer>();

        for (int i=0; i<numCourses; i++) {
            if (inDegree[i] == 0) {
                q.offer(i);
            }
        }

        int insertedInQ = 0;

        while (!q.isEmpty()) {
            int c = q.poll();
            insertedInQ++;

            if (graph.containsKey(c)) {
                HashSet<Integer> dependsOn = graph.get(c);

                for (int d: dependsOn) {
                    inDegree[d]--;

                    if (inDegree[d] == 0) {
                        q.offer(d);
                    }
                }
            }

        }

        return insertedInQ == numCourses;
    }

