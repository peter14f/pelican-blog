200-number_of_islands
#####################

:date: 2016-1-24 21:31
:tags: Blob Detection, Connected Components, BFS
:category: LeetCode
:slug: 200-number_of_islands

`LeetCode Problem Link <https://leetcode.com/problems/number-of-islands/>`_

There is the iterative approach using a kernel, but the details of the implementation are quite difficult to remember.
I therefore much prefer the BFS approach shown below.

.. code-block:: java

    class Cell {
        int x;
        int y;

        public Cell(int row, int col) {
            x = col;
            y = row;
        }
    }

    public int numIslands(char[][] grid) {
        int m = grid.length;
        if (m == 0)
            return 0;
        int n = grid[0].length;

        boolean[][] visited = new boolean[m][n];
        int[][] island = new int[m][n];

        int nextLabel = 1;
        ArrayList<Cell> q = new ArrayList<Cell>();

        for (int row=0; row<m; row++) {
            for (int col=0; col<n; col++) {
                if (grid[row][col] == '1' && !visited[row][col]) {

                    q.add(new Cell(row, col));
                    visited[row][col] = true;

                    int label = nextLabel;
                    nextLabel++;

                    while (!q.isEmpty()) {
                        Cell c = q.remove(0);
                        island[c.y][c.x] = label;

                        // up
                        if (c.y - 1 >= 0 && grid[c.y-1][c.x] == '1' && !visited[c.y-1][c.x]) {
                            visited[c.y-1][c.x] = true;
                            q.add(new Cell(c.y-1, c.x));
                        }

                        // down
                        if (c.y + 1 < m && grid[c.y+1][c.x] == '1' && !visited[c.y+1][c.x]) {
                            visited[c.y+1][c.x] = true;
                            q.add(new Cell(c.y+1, c.x));
                        }

                        // left
                        if (c.x - 1 >= 0 && grid[c.y][c.x-1] == '1' && !visited[c.y][c.x-1]) {
                            visited[c.y][c.x-1] = true;
                            q.add(new Cell(c.y, c.x-1));
                        }

                        // right
                        if (c.x + 1 < n && grid[c.y][c.x+1] == '1' && !visited[c.y][c.x+1]) {
                            visited[c.y][c.x+1] = true;
                            q.add(new Cell(c.y, c.x+1));
                        }
                    }
                }
            }
        }

        return nextLabel - 1;
    }
