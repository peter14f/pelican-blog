041-first_missing_positive
##########################

:date: 2015-9-27 19:50
:tags:
:category: LeetCode
:slug: 041-first_missing_positive

`LeetCode Problem Link <https://leetcode.com/problems/first-missing-positive/>`_

Finding the smallest positive number seen so far would not work.
Can't believe I gave that as an answer during a phone interview.

I said sorting next. But failed to deal with duplicates.

.. code-block:: java

    public int firstMissingPositive(int[] nums) {

        int smallest = Integer.MAX_VALUE;

        for (int i=0; i<nums.length; i++) {
            if (nums[i] <= 0)
                continue;

            if (nums[i] < smallest) {
                smallest = nums[i];
            }
        }

        return smallest + 1;
    }

Asked the runtime complexity. This is clearly O(nlogn).

Here's the O(n) space and O(1) time solution using a hash table.

.. code-block:: java

    public int firstMissingPositive(int[] nums) {

        HashSet<Integer> positiveNums = new HashSet<Integer>();

        for (int i=0; i<nums.length; i++) {
            if (nums[i] > 0) {
                positiveNums.add(nums[i]);
            }
        }

        int i=1;

        while (true) {
            if (!positiveNums.contains(i))
                return i;
            i++;
        }
    }

Finally this is the O(n) time and O(1) space solution.

This is O(n) time because there are at most ``n`` items to be swapped.

The idea is the same as bucket sort. We can place 1 at index 0, 2 at index 1, 3 and index 2, and so on.

The right location for positive integer ``x`` is ``x-1``.

.. code-block:: java

    public int firstMissingPositive(int[] nums) {

        for (int i=0; i<nums.length; i++) {
            if (nums[i] == i+1)
                continue;

            int index = nums[i] - 1;

            if (index >= 0 && index < nums.length && nums[i] != nums[index]) {
                swap(nums, i, index);
                i--; // decrement i because we want to examine the nums[i] again after the swap
            }
        }

        for (int i=0; i<nums.length; i++) {
            if (nums[i] != i+1) {
                return i+1;
            }
        }

        return nums.length+1;
    }


The input array ``nums`` is of size ``n`` and could have integers < 1.

In the first pass, we try to place the number (``nums[i]``) in the correct bin if the number
is >= 1 and <= n. The correct bin is at index ``nums[i] - 1``.

1 should be stored at index 1, 2 should be stored at index 1, ... etc.

We continue swapping the number at index ``i`` with the number at the desired index until either index ``i`` now stores
 the number ``i+1`` or the number at index ``i`` cannot be placed in the desired location. (The number is less than 1 or
 greater than ``n``)

Even though there is a while loop, but there are at most n numbers that need to move to a different bin. So the
first pass takes O(n) time.

In the second pass, we check if ``nums[i] != i + 1`` then ``i+1`` is the first missing positive.
If no such number is found, we return ``n+1``

.. code-block:: java

     public int firstMissingPositive(int[] nums) {

        // at most n numbers will be placed
        for (int i=0; i<nums.length; i++) {

            int num = nums[i];
            int newIndex = num - 1;

            while (num > 0 && newIndex >= 0 && newIndex < nums.length && nums[newIndex] != num) {
                int temp = nums[newIndex];
                nums[newIndex] = num;
                nums[i] = temp;

                num = temp;
                newIndex = num - 1;
            }
        }

        int ans = nums.length + 1;

        for (int i=0; i<nums.length; i++) {
            if (nums[i] != i + 1) {
                ans = i + 1;
                break;
            }
        }

        return ans;
    }