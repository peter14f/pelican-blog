219-contains_duplicate_ii
#########################

:date: 2016-2-1 16:32
:tags: Hash Tables
:category: LeetCode
:slug: 219-contains_duplicate_ii

`LeetCode Problem Link <https://leetcode.com/problems/contains-duplicate-ii/>`_

Sorting wouldn't work in this case because we would lose the information of where an element was originally
stored at. So we can solve this problem in one pass with a HashMap<Integer, Integer>. The key is the
element and the value is the index we last saw the element.

.. code-block:: java

   public boolean containsNearbyDuplicate(int[] nums, int k) {
        HashMap<Integer, Integer> lastIndex = new HashMap<Integer, Integer>();

        for (int i=0; i<nums.length; i++) {
            if (lastIndex.containsKey(nums[i])) {
                int lastSeen = lastIndex.get(nums[i]);
                if (i - lastSeen <= k)
                    return true;
            }

            lastIndex.put(nums[i], i);
        }

        return false;
    }
