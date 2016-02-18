254-factor_combinations
#######################

:date: 2016-2-18 10:52
:tags: Recursion
:category: LeetCode
:slug: 254-factor_combinations

`LeetCode Problem Link <https://leetcode.com/problems/factor-combinations/>`_

I am using recursion to solve this problem. To avoid excessive number of recursive calls, we've got to
make sure that we only make a recursive call for a valid factor.

``factorAhead`` is the previous factor found. The problem wants each list of factors to be in non-decreasing
order.

.. code-block:: java

    // do not return 1 and n
    public List<List<Integer>> getFactors(int n) {
        List<List<Integer>> lists = new ArrayList<List<Integer>>();

        if (n<=1)
            return lists;

        int firstFactorToTry = 2;

        while (firstFactorToTry < n && n%firstFactorToTry != 0) {
            firstFactorToTry++;
        }

        if (firstFactorToTry < n)
            findListsOfFactors(
                    n, firstFactorToTry, new ArrayList<Integer>(),
                    0, lists);

        return lists;
    }

    private void findListsOfFactors(
            int n,
            int factor,
            List<Integer> curList,
            int factorAhead,
            List<List<Integer>> lists) {

        int toRemove = 0;
        int q = n / factor;

        /*
        System.out.println("n=" + n + " factor=" + factor + " q=" +
                            q + " factorAhead=" + factorAhead);
        */

        if (factor <= q) {
            if (factor >= factorAhead) {
                curList.add(factor);
                curList.add(q);
                toRemove = 2;
                lists.add(new ArrayList<Integer>(curList));



                // further decompose q if possible
                if (q > 2) {
                    curList.remove(curList.size()-1);
                    toRemove--;

                    int firstFactorToTry = 2;

                    while (firstFactorToTry < q && q % firstFactorToTry != 0) {
                        firstFactorToTry++;
                    }

                    if (firstFactorToTry < q)
                        findListsOfFactors(q, firstFactorToTry, curList, factor, lists);
                }
            }
        }

        if (toRemove == 2) {
            curList.remove(curList.size()-1);
            curList.remove(curList.size()-1);
        }
        else if (toRemove == 1) {
            curList.remove(curList.size()-1);
        }

        int nextFactorToTry = factor + 1;

        while (nextFactorToTry < n && n%nextFactorToTry != 0) {
            nextFactorToTry++;
        }

        if (nextFactorToTry < n) {
            findListsOfFactors(n, nextFactorToTry, curList, factorAhead, lists);
        }
    }

