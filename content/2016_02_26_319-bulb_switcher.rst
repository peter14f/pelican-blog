319-bulb_switcher
#################

:date: 2016-2-26 23:05
:tags: Brain Teaser
:category: LeetCode
:slug: 319-bulb_switcher

`LeetCode Problem Link <https://leetcode.com/problems/bulb-switcher/>`_

``n`` bulbs are initially OFF.

Toggle every ``k`` bulb starting at round k=1.

So at round zero, all bulbs are ON.

Find how many bulbs are ON after ``n`` rounds.

For ``n <= 0`` return ``0``.

So we are returning a count, not the states of each bulb.

``n`` bulbs ``n`` rounds.

If you simulate ``n`` rounds of ``n`` bulbs, it will take you O(n \ :superscript:`2`) time.

But let's implement this straightforward solution anyways.

.. code-block:: java

    public int bulbSwitch(int n) {
        boolean[] states = new boolean[n];

        for (int i=1; i<=n; i++) {
            for (int j=0; j<n; j++) {
                if (i==1)
                    states[j] = !states[j];
                else if ((j+1)%i == 0)
                    states[j] = !states[j];

            }
        }

        int cnt = 0;
        for (int j=0; j<n; j++) {
            if (states[j])
                cnt++;
        }

        //System.out.println(Arrays.toString(states));

        return cnt;
    }

You guessed it! TLE on large Test Case.

::

    Submission Result: Time Limit Exceeded More Details
    Last executed input:
    99999

It looks like the answer to ``n`` can be derived from the answer to ``n-1``.

The number of times the last bulb is flipped determines if the answer to ``n`` is one more of the answer to ``n-1``.

If the number is even, then we add 1 to the answer to ``n-1``.
If the number is odd, then the answer to ``n`` is simply the same as the answer to ``n-1``.

.. code-block:: java

    public int bulbSwitch(int n) {

        int ans = 1;

        for (int i=2; i<=n; i++) {

            int cnt = 1;


            for (int j=2; j<i; j++) {
                if (i % j == 0) {
                    cnt++;
                }
            }

            //System.out.println("n=" + i + " cnt=" + cnt + " prevAns=" + ans);


            if (cnt % 2 == 0)
                ans++;

        }

        return ans;
    }



This is still O(n \ :superscript:`2`) time.

If we consider the ith ball only. The ith bulb gets toggled when ``i`` is a multiple of some integer in the range [1, n].

i=1 1*1
i=2 1*2, 2*1
i=3 1*3, 3*1
i=4 1*4, 2*2, 4*1
i=5 1*5, 5*1
i=6 1*6, 2*3, 3*2, 6*1
i=7 1*7, 7*1
i=8 1*8, 2*4, 4*2, 8*1
i=9 1*9, 3*3, 9*1

In the previous approach we were essentially counting the number of times ``i`` is a multiple of some integer
in the range [2, n-1].

What you should notice is that only when ``i = x*x`` for some integer ``x`` would the number of times ``i`` is
a multiple for some integer in the range [1, n] be odd. Look at i=4 and i=9.

.. code-block:: java

    public int bulbSwitch(int n) {
        return (int) Math.sqrt(n);
    }




