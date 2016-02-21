279-perfect_squares
###################

:date: 2016-2-21 1:10
:tags: BFS, DFS, Dynamic Programming
:category: LeetCode
:slug: 279-perfect_squares

`LeetCode Problem Link <https://leetcode.com/problems/perfect-squares/>`_

Find the least number of **perfect square numbers** that sum to ``n``

If there is an int ``i`` such that ``i * i = n`` then the answer is ``1``.

DFS solution gives us TLE. Basically, I am looking for all combination sums of perfect squares that
that sums up to ``n`` and look for the shortest combination.

.. code-block:: java

    public int numSquares(int n) {
        if (n<1)
            return 0;

        int sqrt = (int) Math.sqrt(n);

        if (sqrt*sqrt == n)
            return 1;

        List<List<Integer>> lists = new ArrayList<List<Integer>>();

        findCombinationSum(1, 0, new ArrayList<Integer>(), n, lists);

        //System.out.println(lists);

        if (lists.isEmpty())
            return 0;

        int min = lists.get(0).size();

        for (int i=1; i<lists.size(); i++) {
            if (lists.get(i).size() < min) {
                min = lists.get(i).size();
            }
        }

        return min;
    }

    private void findCombinationSum(int i, int curSum, List<Integer> curList,
                                    int target, List<List<Integer>> ans) {
        int squared = i * i;

        if (curSum + squared > target)
            return;

        int oldCurSum = curSum;
        int toRemove = 0;

        while (curSum + squared <= target) {
            curSum += squared;
            curList.add(i);

            if (curSum == target) {
                ans.add(new ArrayList<Integer>(curList));
            }
            toRemove++;

            if (curSum < target)
                findCombinationSum(i+1, curSum, curList, target, ans);
        }

        while (toRemove > 0) {
            curList.remove(curList.size() - 1);
            toRemove--;
        }

        findCombinationSum(i+1, oldCurSum, curList, target, ans);
    }

Now I thought of using BFS. The queues end up being too long.

.. code-block:: java

    public int numSquares(int n) {
        if (n<1)
            return 0;

        int sqrt = (int) Math.sqrt(n);

        if (sqrt*sqrt == n)
            return 1;

        List<List<Integer>> lists = new ArrayList<List<Integer>>();

        findCombinationSum(1, 0, new ArrayList<Integer>(), n, lists);

        //System.out.println(lists);

        if (lists.isEmpty())
            return 0;

        int min = lists.get(0).size();

        for (int i=1; i<lists.size(); i++) {
            if (lists.get(i).size() < min) {
                min = lists.get(i).size();
            }
        }

        return min;
    }

    private void findCombinationSum(int i, int curSum, List<Integer> curList,
                                    int target, List<List<Integer>> ans) {
        int squared = i * i;

        if (curSum + squared > target)
            return;

        int oldCurSum = curSum;
        int toRemove = 0;

        while (curSum + squared <= target) {
            curSum += squared;
            curList.add(i);

            if (curSum == target) {
                ans.add(new ArrayList<Integer>(curList));
            }
            toRemove++;

            if (curSum < target)
                findCombinationSum(i+1, curSum, curList, target, ans);
        }

        while (toRemove > 0) {
            curList.remove(curList.size() - 1);
            toRemove--;
        }

        findCombinationSum(i+1, oldCurSum, curList, target, ans);
    }

So we must use dynamic programming. Initialize an int array of size ``n+1`` called ``numSquares``.

``numSquares[0]`` is initialized to ``0`` and all other entries are initialized to ``Integer.MAX_VALUE``.

``numSquares[i]`` is the minimum number of perfect squares that sum up to ``i``.


I didn't quite get why the ``+1`` in the equation. But here's a good explanation.

if x = a + b*b then minSquare(x) = 1 + minSquare(a) because b*b is already a perfect squared number.

.. code-block:: java

    public int numSquares(int n) {
        int[] numSquares = new int[n+1];

        for (int i=1; i<=n; i++) {
            numSquares[i] = i; // i 1s is max

            for (int j=1; j*j <= i; j++) {
                numSquares[i] = Math.min(numSquares[i],
                                         numSquares[i - j*j] + 1);
            }
        }

        return numSquares[n];
    }

