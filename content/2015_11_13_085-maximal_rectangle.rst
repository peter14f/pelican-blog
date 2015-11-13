085-maximal_rectangle
#####################

:date: 2015-11-13 13:32
:tags: Max Rectangle Area
:category: LeetCode
:slug: 085-maximal_rectangle

`LeetCode Problem Link <https://leetcode.com/problems/maximal-rectangle/>`_

We can use the solution to 084-largest_rectangle_in_histogram to solve this problem. Create another 2D int array
called ``height`` that's of the same size to the input 2D char array. What we store in height[r][c] is the height
of the histogram if row ``r`` is considered the ground level. In other words, count the number of consecutive
``1``s above (and including row ``r``) row ``r``. We do this for all cells in ``height``.

Once this 2D array ``height`` is built. We need to call getMaxRectangleInHistogram on all rows of ``height``. Note that
each row of ``height`` is itself a 1D int array. Whichever row gives us the largest area will be our final answer.

.. code-block:: java

    // find the largest rectangle filled with '1's
    public int maximalRectangle(char[][] matrix) {
        if (matrix==null || matrix.length==0)
            return 0;

        int m = matrix.length;
        int n = matrix[0].length;

        int[][] height = new int[m][n];

        for (int col=0; col < n; col++) {
            int cnt = 0;

            for (int row=0; row < m; row++) {
                if (matrix[row][col]=='1')
                    cnt++;
                else
                    cnt = 0;

                height[row][col] = cnt;
            }
        }

        System.out.println(Arrays.deepToString(height));

        int maxRectangle = 0;

        for (int row=0; row < m; row++) {
            int[] histogram = height[row];
            int area = getMaxRectangle(histogram);
            System.out.println("row " + row + " area=" + area);
            if (area > maxRectangle)
                maxRectangle = area;
        }

        return maxRectangle;
    }

    private int getMaxRectangle(int[] height) {
        if (height==null || height.length == 0)
            return 0;

        // stk stores the index, not the height
        Stack<Integer> stk = new Stack<Integer>();
        int i=0;
        int maxArea = 0;

        while (!stk.isEmpty() || i<height.length) {
            if (stk.isEmpty()) {
                stk.push(i);
                i++;
                continue;
            }

            if (i == height.length || height[i] < height[stk.peek()]) {
                int poppedIndex = stk.pop();

                int prevShorterIndex = -1;

                if (!stk.isEmpty()) {
                    prevShorterIndex = stk.peek();
                }

                int area = height[poppedIndex]*(i - (prevShorterIndex + 1));
                if (area > maxArea) {
                    maxArea = area;
                }
            }
            else {
                stk.push(i);
                i++;
                continue;
            }
        }

        return maxArea;
    }

