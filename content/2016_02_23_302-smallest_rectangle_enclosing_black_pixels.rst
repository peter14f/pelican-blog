302-smallest_rectangle_enclosing_black_pixels
#############################################

:date: 2016-2-23 18:21
:tags: BFS, Blob Analysis
:category: LeetCode
:slug: 302-smallest_rectangle_enclosing_black_pixels

`LeetCode Problem Link <https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels/>`_

``0`` as white pixel and ``1`` as black pixel.

``x`` specifies the row and ``y`` specifies the col. I find this kind of weird.

This problem is essentially asking you to do a blob analysis and find out the blob's minX, minY, maxX, and maxY.

The smallest rectangle enclosing the black blob is simply ``(maxX - minX + 1) * (maxY - minY + 1)``.

4-connected components are considered neighbors in this problem, not 8.

BFS would work.

.. code-block:: java

    class Cell {
        int row;
        int col;

        public Cell(int r, int c) {
            row = r;
            col = c;
        }

        public int hashCode() {
            return row * 10 + col;
        }

        public boolean equals(Object c) {
            Cell cc = (Cell)c;
            return (row == cc.row && col == cc.col);
        }
    }

    public int minArea(char[][] image, int x, int y) {
        if (image[x][y] == '0')
            return 0;

        int m = image.length;

        if (m==0)
            return 0;

        int n = image[0].length;

        int minCol = y;
        int maxCol = y;

        int minRow = x;
        int maxRow = x;

        Queue<Cell> q = new LinkedList<Cell>();
        HashSet<Cell> visited = new HashSet<Cell>();
        Cell start = new Cell(x, y);
        q.add(start);
        visited.add(start);

        while (!q.isEmpty()) {
            Cell c = q.poll();

            //System.out.println("row=" + c.row + " col=" + c.col);

            minCol = Math.min(minCol, c.col);

            maxCol = Math.max(maxCol, c.col);

            minRow = Math.min(minRow, c.row);

            maxRow = Math.max(maxRow, c.row);

            // up
            if (c.row - 1 >= 0 && image[c.row-1][c.col] == '1') {
                Cell up = new Cell(c.row-1, c.col);
                if (!visited.contains(up)) {
                    visited.add(up);
                    q.offer(up);
                }
            }

            // down
            if (c.row + 1 < m && image[c.row+1][c.col] == '1') {
                Cell down = new Cell(c.row+1, c.col);
                if (!visited.contains(down)) {
                    visited.add(down);
                    q.offer(down);
                }
            }

            // left
            if (c.col - 1 >= 0 && image[c.row][c.col-1] == '1') {
                Cell left = new Cell(c.row, c.col-1);
                if (!visited.contains(left)) {
                    visited.add(left);
                    q.offer(left);
                }
            }

            // right
            if (c.col + 1 < n && image[c.row][c.col+1] == '1') {
                Cell right = new Cell(c.row, c.col+1);
                if (!visited.contains(right)) {
                    visited.add(right);
                    q.offer(right);
                }
            }

        }

        //System.out.println("minRow=" + minRow + " maxRow=" + maxRow);
        //System.out.println("minCol=" + minCol + " maxCol=" + maxCol);

        return (maxCol-minCol+1)*(maxRow-minRow+1);
    }

