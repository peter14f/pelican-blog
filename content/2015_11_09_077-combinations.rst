077-combinations
################

:date: 2015-11-9 13:06
:tags: Combinations, Recursion
:category: LeetCode
:slug: 077-combinations

`LeetCode Problem Link <https://leetcode.com/problems/combinations/>`_

I solved this problem in the same manner that I solved a lot of the NP problems.
``choices`` is the list of integers that's left to choose from.
``curList`` is the list we've build up so far.
Once the size of ``curList`` has reached ``k`` then we know we've just found another combination.

.. code-block:: java

    public List<List<Integer>> combine(int n, int k) {

        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        if (k == 0)
            return ans;
        if (k < 0)
            throw new IllegalArgumentException();

        LinkedList<Integer> choices = new LinkedList<Integer>();

        for (int i=1; i<=n; i++) {
            choices.add(i);
        }


        List<Integer> curList = new ArrayList<Integer>();

        combine(choices, curList, ans, k);

        return ans;
    }

    private void combine(
            LinkedList<Integer> choices,
            List<Integer> curList,
            List<List<Integer>> ans,
            int k) {

        int numChoices = choices.size();
        Stack<Integer> removed = new Stack<Integer>();

        if (numChoices + curList.size() < k)
            return;

        for (int i=0; i<numChoices; i++) {
            int choice = choices.removeFirst();

            curList.add(choice);
            if (curList.size() == k) {
                ans.add(new ArrayList<Integer>(curList));
            }

            if (!choices.isEmpty())
                combine(choices, curList, ans, k);

            curList.remove(curList.size() - 1);
            removed.push(choice);
        }

        while (!removed.isEmpty()) {
            choices.addFirst(removed.pop());
        }
    }
