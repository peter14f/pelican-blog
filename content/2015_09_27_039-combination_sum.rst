039-combination_sum
###################

:date: 2015-9-27 10:51
:tags: DFS, NP
:category: LeetCode
:slug: 039-combination_sum

`LeetCode Problem Link <https://leetcode.com/problems/combination-sum/>`_

Sort ``candidates`` first so that the search can stop immediately if the current
sum exceeds ``target``. I keep a ``workingList`` and only do a deep copy
when the current sum reaches target. We must make sure that every ``add`` is accompanied
with a ``remove`` so that the workingList maintains the original size at the caller.

In this particular problem, ``candidates`` does not have duplicate items.

.. code-block:: java

    public List<List<Integer>> combinationSum(int[] candidates, int target) {

        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        List<Integer> workingList = new ArrayList<Integer>();
        int curSum = 0; // current sum in working list

        Arrays.sort(candidates);
        combinationSum(candidates, target, 0, workingList, curSum, ans);

        return ans;
    }

    private void combinationSum(int[] candidates, int target, int index,
                                List<Integer> workingList, int curSum,
                                List<List<Integer>> ans) {

        int num = candidates[index];
        int oldSize = workingList.size();

        if (curSum + num == target) {
            workingList.add(num);
            ans.add(new ArrayList<Integer>(workingList));
            workingList.remove(workingList.size() - 1);
        }
        else if (curSum + num < target) {

            // do not include num
            combinationSum(candidates, target, index + 1, workingList, curSum, ans);

            // include num up to n times
            int newSum = curSum + num;
            int cnt = 0;

            while (newSum < target) {
                cnt++;
                workingList.add(num);
                combinationSum(candidates, target, index + 1, workingList, newSum, ans);

                newSum += num;
            }

            if (newSum == target) {
                workingList.add(num);
                ans.add(new ArrayList<Integer>(workingList));
                workingList.remove(workingList.size() - 1);
            }

            for (int i=0; i<cnt; i++) {
                workingList.remove(workingList.size() - 1);
            }
        }

    }

