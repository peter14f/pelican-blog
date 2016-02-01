217-contains_duplicate
######################

:date: 2016-2-1 15:49
:tags: Hash Tables
:category: LeetCode
:slug: 217-contains_duplicate

`LeetCode Problem Link <https://leetcode.com/problems/contains-duplicate/>`_

There are two ways to do this problem. The first approach uses a HashSet<Integer> and can detect the duplicated
item in one pass.

.. code-block:: java

    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> set = new HashSet<Integer>();

        for (int i=0; i<nums.length; i++) {
            if (set.contains(nums[i]))
                return true;
            else
                set.add(nums[i]);
        }

        return false;
    }

The second way is to sort the array first and then the duplicated items will be adjacent to one another.
