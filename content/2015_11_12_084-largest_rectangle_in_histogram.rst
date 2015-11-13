084-largest_rectangle_in_histogram
##################################

:date: 2015-11-12 19:43
:tags: Max Rectangle Area, Histogram
:category: LeetCode
:slug: 084-largest_rectangle_in_histogram

`LeetCode Problem Link <https://leetcode.com/problems/largest-rectangle-in-histogram/>`_

Using the height at a particular index to calculate the area, we must find the first bar to the right that's smaller
and the first bar to the left that's smaller. We will use a stack.

.. code-block:: java

    public int largestRectangleArea(int[] height) {

        if (height==null || height.length == 0)
            return 0;

        int maxArea = 0;

        // stack stores the index
        Stack<Integer> stk = new Stack<Integer>();

        int i = 0;

        while (i < height.length || !stk.isEmpty()) {
            if (stk.isEmpty()) {
                stk.push(i);
                i++;
                continue;
            }

            if (i==height.length || height[i] < height[stk.peek()]) {
                int poppedIndex = stk.pop();
                int peepIndex = -1;

                if (!stk.isEmpty()) {
                    peepIndex = stk.peek();
                }

                // time to calculate the area
                int area = height[poppedIndex]*(i - (peepIndex+1));
                if (area > maxArea)
                    maxArea = area;
            }
            else {
                stk.push(i);
                i++;
            }
        }

        return maxArea;
    }

TThe time complexity is O(n) because every height gets pushed on the stack and the area using it as the height
gets calculated once when it's popped.