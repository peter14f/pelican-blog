046-permutations
################

:date: 2015-10-4 17:21
:tags: Recursion, NP, Permutations
:category: LeetCode
:slug: 046-permutations

`LeetCode Problem Link <https://leetcode.com/problems/permutations/>`_


There are two ways to think about this problem.

The first way is what I call the "inserting the current number" way.
It uses recursion and relies on the answer to a smaller problem.

  1. In the solution ``l`` refers to the starting index of elements to be considered in the input. ``h`` refers
     to the ending index of elements to be considered in the input. So when ``h == l``, the input has only one element.

.. code-block:: java

    public List<List<Integer>> permute(int[] nums) {
        return permute(nums, 0, nums.length - 1);
    }

    private List<List<Integer>> permute(int[] nums, int l, int h) {

        if (nums.length == 0) {
            return new ArrayList<List<Integer>>();
        }
        else if (h == l) {
            List<List<Integer>> ans = new ArrayList<List<Integer>>();
            List<Integer> list = new ArrayList<Integer>();
            list.add(nums[l]);
            ans.add(list);
            return ans;
        }
        else {
            int myNumber = nums[l];
            List<List<Integer>> lists = permute(nums, l+1, h);
            List<List<Integer>> ans = new ArrayList<List<Integer>>();

            for (List<Integer> list : lists) {
                int oldSize = list.size();
                int newSize = oldSize + 1;

                for (int j=0; j<newSize; j++) {
                    List<Integer> newList = new ArrayList<Integer>();
                    Iterator<Integer> iter = list.iterator();

                    while (newList.size() < newSize) {
                        if (newList.size() == j) {
                            newList.add(myNumber);
                        }
                        else {
                            newList.add(iter.next());
                        }
                    }

                    ans.add(newList);
                }
            }

            return ans;
        }

    }


The second way is what I call the "try these numbers out" way.

  The way to implement this is very close to
  040-combination_sum. Each time the function is called, a number is from the ``nums`` list
  and inserted into the ``curWorkingList``, when the size of ``curWorkingList`` reaches the size of ``nums``, we
  know that ``curWorkingList`` is one permutation.

.. code-block:: java

    public List<List<Integer>> permute(int[] nums) {

        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        List<Integer> curWorkingList = new ArrayList<Integer>();
        boolean[] tried = new boolean[nums.length];

        permute(nums, tried, curWorkingList, ans);

        return ans;
    }

    private void permute(int[] nums,
                         boolean[] tried,
                         List<Integer> curWorkingList,
                         List<List<Integer>> ans) {

        if (curWorkingList.size() == nums.length) {
            ans.add(new ArrayList<Integer>(curWorkingList));
            return;
        }

        for (int i=0; i<nums.length; i++) {
            if (!tried[i]) {
                curWorkingList.add(nums[i]);
                tried[i] = true;
                permute(nums, tried, curWorkingList, ans);
                curWorkingList.remove(curWorkingList.size() - 1);
                tried[i] = false;
            }
        }
    }