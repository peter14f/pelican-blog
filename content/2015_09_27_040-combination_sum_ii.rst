040-combination_sum_ii
######################

:date: 2015-9-27 11:04
:tags: DFS, NP
:category: LeetCode
:slug: 040-combination_sum_ii

`LeetCode Problem Link <https://leetcode.com/problems/combination-sum-ii/>`_

Unlike **040-combination_sum**, ``candidates`` can have duplicates.

So the tricky part is to make sure that we do not have duplicates in the answer.

For example, ``candidates={1, 1, 1, 2}`` and ``target=3``.

We want to make sure ``ans={{1, 1, 1}, {1, 2}}``

In other words, ``{1, 2}`` occurs only once in the answer.

How do we do this?

In the code path where we are NOT including the current number in
the ``workingList``, we will skip all the following indices that
also have the same number as the current number.

.. code-block:: java

    public List<List<Integer>> combinationSum2(int[] candidates, int target) {

        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        List<Integer> workingList = new ArrayList<Integer>();
        int curSum = 0;

        Arrays.sort(candidates);
        combinationSum2(candidates, target, 0, workingList, curSum, ans);

        return ans;
    }

    private void combinationSum2(int[] candidates, int target, int index, List<Integer> workingList,
                                 int curSum, List<List<Integer>> ans) {

        int num = candidates[index];

        if (curSum + num == target) {
            workingList.add(num);
            ans.add(new ArrayList<Integer>(workingList));
            workingList.remove(workingList.size() - 1);
        }
        else if (curSum + num < target) {
            // choose not to include num
            int d = 1;

            while (index + d < candidates.length && candidates[index+d] == num) {
                d++;
            }
            if (index + d < candidates.length)
                combinationSum2(candidates, target, index + d, workingList, curSum, ans);

            // include num
            workingList.add(num);
            if (index + 1 < candidates.length)
                combinationSum2(candidates, target, index + 1, workingList, curSum + num, ans);
            workingList.remove(workingList.size() - 1);
        }
    }

