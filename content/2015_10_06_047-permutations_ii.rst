047-permutations_ii
###################

:date: 2015-10-6 16:32
:tags: Recurstion, NP
:category: LeetCode
:slug: 047-permutations_ii

`LeetCode Problem Link <https://leetcode.com/problems/permutations-ii/>`_

The solution is based on the "try these number out" method mentioned in the previous problem.

We sort the array ``nums`` first, so that we can check for duplicates more easily.

.. code-block:: java

    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        List<Integer> curWorkingList = new ArrayList<Integer>();
        boolean[] tried = new boolean[nums.length];
        Arrays.sort(nums);

        permuteUnique(nums, tried, curWorkingList, ans);

        return ans;
    }

    private void permuteUnique(int[] nums,
                               boolean[] tried,
                               List<Integer> curWorkingList,
                               List<List<Integer>> ans) {

        if (curWorkingList.size() == nums.length) {
            ans.add(new ArrayList<Integer>(curWorkingList));
            return;
        }

        for (int i=0; i<nums.length; i++) {
            if (!tried[i]) {
                if (i-1 >= 0 && nums[i] == nums[i-1] && !tried[i-1]) {
                    continue;
                }
                tried[i] = true;
                curWorkingList.add(nums[i]);
                permuteUnique(nums, tried, curWorkingList, ans);
                curWorkingList.remove(curWorkingList.size() - 1);
                tried[i] = false;
            }
        }
    }