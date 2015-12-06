128-longest_consecutive_sequence
################################

:date: 2015-12-5 23:04
:tags:
:category: LeetCode
:slug: 128-longest_consecutive_sequence

`LeetCode Problem Link <https://leetcode.com/problems/longest-consecutive-sequence/>`_

This problem can be done using one HashSet of integers. We first insert all the numbers in the array into
the Hashset. Then as we go through each number in the int array, we use the HashSet to quickly look up if
the adjacent numbers are also in the input array. If so, we remove the number from the HashSet so that
we don't attempt to find the sequence for that number again.

.. code-block:: java

    public int longestConsecutive(int[] nums) {

        if (nums.length ==0)
            return 0;

        HashSet<Integer> numbers = new HashSet<Integer>();

        for (int i=0; i<nums.length; i++)
            numbers.add(nums[i]);

        int maxLength = 0;

        for (int i=0; i<nums.length; i++) {
            if (numbers.contains(nums[i])) {
                int length = consectiveSequenceLength(nums, i, numbers);

                if (length > maxLength)
                    maxLength = length;
            }
        }

        return maxLength;
    }

    private int consectiveSequenceLength(
            int[] nums, int index,
            HashSet<Integer> numbers) {

        int x = nums[index];

        int small = x - 1;
        int leftLength = 0;

        while (numbers.contains(small)) {
            numbers.remove(small);
            leftLength++;
            small--;
        }

        int big = x + 1;
        int rightLength = 0;

        while (numbers.contains(big)) {
            numbers.remove(big);
            rightLength++;
            big++;
        }

        return 1 + rightLength + leftLength;
    }

This approach takes O(n) time and O(n) which satisfies the requirement in the problem statement.
