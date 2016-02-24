299-bulls_and_cows
##################

:date: 2016-2-23 10:14
:tags:
:category:
:slug: 299-bulls_and_cows

`LeetCode Problem Link <https://leetcode.com/problems/bulls-and-cows/>`_

# of bulls = right number at the right location

We can do this problem in two passes.

In the first pass, if the secret and guess characters don't match. We increment the count for that guess character
in int[] guesses. else increment ``bulls``.

In the second pass, if the secret and guess characters don't match. We check if the count for that secret character
is greater than 0. If so, increment ``cows`` and decrement that cnt in ``guesses``.

.. code-block:: java

    public String getHint(String secret, String guess) {

        int n = secret.length();

        if (n==0)
            return "0A0B";

        int bulls = 0;

        int[] guesses = new int[10];

        int cows = 0;

        for (int i=0; i<n; i++) {
            char s = secret.charAt(i);
            char g = guess.charAt(i);
            if (s == g) {
                bulls++;
            }
            else {
                guesses[g - '0']++;
            }
        }

        for (int i=0; i<n; i++) {
            char s = secret.charAt(i);
            char g = guess.charAt(i);

            if (s != g) {
                if (guesses[s - '0'] > 0) {
                    cows++;

                    guesses[s - '0']--;
                }
            }
        }

        StringBuffer sb = new StringBuffer();
        sb.append(bulls);
        sb.append("A");
        sb.append(cows);
        sb.append("B");

        return sb.toString();
    }

This approach takes O(10) space and O(n) time.

Otherwise, we could also do it in O(1) space and O(n \ :superscript:`2`) time.