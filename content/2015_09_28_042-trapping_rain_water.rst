042-trapping_rain_water
#######################

:date: 2015-9-28 15:59
:tags: water
:category: LeetCode
:slug: 042-trapping_rain_water

`LeetCode Problem Link <https://leetcode.com/problems/trapping-rain-water/>`_

The straightforward solution take O(n\ :superscript:`2`) time.


For each height at index ``i``

  | Find its tallest left wall and its tallest right wall if available.
  | volume += Math.min(rightWall, leftWall) - height[i]

.. code-block:: java

    public int trap(int[] height) {
        int volume = 0;

        for (int i=0; i<height.length; i++) {
            int leftPeak = height[i];
            int rightPeak = height[i];

            // find left peak
            for (int l=i-1; l >=0; l--) {
                if (height[l] > leftPeak)
                    leftPeak = height[l];
            }

            if (leftPeak <= height[i])
                continue;

            // find right peak
            for (int r=i+1; r < height.length; r++) {
                if (height[r] > rightPeak)
                    rightPeak = height[r];
            }

            if (leftPeak > height[i] && rightPeak > height[i]) {
                volume += Math.min(leftPeak, rightPeak) - height[i];
            }
        }

        return volume;
    }

| The optimal solution takes only O(n) time.
| We use two pointers ``left`` and ``right``
| In each iteration, we move the pointer that has the smaller height

.. code-block:: java

    public int trap2(int[] height) {

        if (height.length == 0)
            return 0;

        int volume = 0;

        int leftWall = height[0];
        int rightWall = height[height.length - 1];

        int left = 0;
        int right = height.length - 1;

        while (left <= right) {
            if (height[right] > rightWall)
                rightWall = height[right];

            if (height[left] > leftWall)
                leftWall = height[left];

            if (height[left] <= height[right]) {

                volume += Math.min(rightWall, leftWall) - height[left];
                left++;
            }
            else {

                volume += Math.min(rightWall, leftWall) - height[right];
                right--;
            }
        }

        return volume;
    }