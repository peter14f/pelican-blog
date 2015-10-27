060-permutation_sequence
########################

:date: 2015-10-26 19:24
:tags: Permutations
:category: LeetCode
:slug: 060-permutation_sequence

`LeetCode Problem Link <https://leetcode.com/problems/permutation-sequence/>`_

Store all the choices in a list first. Then calculat for each digit which choice should be used. Once used, remove that
choice from the list.

.. code-block:: java

    public String getPermutation(int n, int k) {
        if (n<=0 || k <= 0)
            return "";

        int factorial = 1;
        List<Integer> choices = new ArrayList<Integer>();
        StringBuffer sb = new StringBuffer();

        for (int i=1; i<=n; i++) {
            factorial = factorial * i;
            choices.add(i);
        }

        k = k - 1;

        for (int i=n; i>0; i--) {
            factorial = factorial / i;
            int index = k / factorial;
            int digit = choices.remove(index);
            sb.append(digit);
            k = k % factorial;
        }

        return sb.toString();
    }
