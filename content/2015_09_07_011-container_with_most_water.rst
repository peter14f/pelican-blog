011-container_with_most_water
#############################

:date: 2015-9-7 20:12
:tags: water
:category: LeetCode
:slug: 011-container_with_most_water

`LeetCode Problem Link <https://leetcode.com/problems/trapping-rain-water/>`_

Well the straightforward O(n\ superscript:``2``) solution is easy.


For left bar located at index ``i``

  Compute the area formed with all the possible right bars located at index ``j``



| Here is the O(n) time solution
| Use two pointers ``left`` and ``right``.
| Let ``left`` start at ``0`` and ``right`` start at ``n-1``.
| Calculate the area given the formed by bars located at ``left`` and ``right``.
| Shift the pointer with a shorter bar.


.. code-block:: java

    public int maxArea(int[] height) {

        if (height.length == 0 || height.length == 1)
            return 0;

        int left = 0;
        int right = height.length - 1;
        int maxArea = 0;

        while (left < right) {

            int volume = (right - left) * Math.min(height[left], height[right]);
            if (volume > maxArea)
                maxArea = volume;

            if (height[left] <= height[right]) {
                left++;
            }
            else {
                right--;
            }
        }

        return maxArea;
    }