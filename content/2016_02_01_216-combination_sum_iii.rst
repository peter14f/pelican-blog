216-combination_sum_iii
#######################

:date: 2016-2-1 15:25
:tags: NP, recursion, DFS
:category: LeetCode
:slug: 216-combination_sum_iii

`LeetCode Problem Link <https://leetcode.com/problems/combination-sum-iii/>`_

When we see a new number, we have two choices, choose to include it in the list or choose not
to include it in the list. Since ``choices`` was built by ourselves, we make sure it's sorted.
This makes it easier to break out from the recursion as early as possible. When the ``curSum``
already exceeds ``target``, we know there is no point looking further down in the ``choices``
list since future choices will only be even larger.

.. code-block:: java

    public List<List<Integer>> combinationSum3(int k, int n) {
        List<List<Integer>> ans = new ArrayList<List<Integer>>();

        if (k<=0)
            return ans;

        List<Integer> choices = new ArrayList<Integer>();

        for (int i=1; i<=9; i++)
            choices.add(i);

        combinationSum(choices, 0, n, k, new ArrayList<Integer>(), 0, ans);

        return ans;
    }

    private void combinationSum(List<Integer> choices,
                                int index,
                                int target, int size,
                                List<Integer> curList, int curSum,
                                List<List<Integer>> ans) {

        if (index==choices.size())
            return;

        // choose to include choice at index
        int choice = choices.get(index);
        int newSum = curSum + choice;
        int newSize = curList.size() + 1;

        if (newSum <= target && newSize <= size) {
            curList.add(choice);

            if (newSum == target && newSize == size) {
                ans.add(new ArrayList<Integer>(curList));
            }
            else {
                combinationSum(choices, index+1, target, size, curList, newSum, ans);
            }

            curList.remove(curList.size()-1);
        }

        // choose not to include choice at index
        combinationSum(choices, index+1, target, size, curList, curSum, ans);
    }