243-shortest_word_distance
##########################

:date: 2016-2-17 1:01
:tags:
:category: LeetCode
:slug: 243-shortest_word_distance

`LeetCode Problem Link <https://leetcode.com/problems/shortest-word-distance/>`_

The problem statement states that ``word1`` and ``word2`` are different strings and they are both in the
input array.

But please note that the strings in the input array may repeat.

We can do this in one-pass. We just need to keep track of the current minimum distance and where we last saw
``word1`` and ``word2``.

.. code-block:: java

    public int shortestDistance(String[] words, String word1, String word2) {
        int latest1 = Integer.MIN_VALUE;
        int latest2 = Integer.MIN_VALUE;
        int minDistance = Integer.MAX_VALUE;

        for (int i=0; i<words.length; i++) {
            if (word1.equals(words[i])) {
                if (latest2 >= 0) {
                    int distance = i - latest2;
                    if (distance < minDistance)
                        minDistance = distance;
                }

                latest1 = i;
            }
            else if (word2.equals(words[i])) {
                if (latest1 >= 0) {
                    int distance = i - latest1;
                    if (distance < minDistance)
                        minDistance = distance;
                }

                latest2 = i;
            }
        }

        return minDistance;
    }

The time complexity is O(n) where ``n`` is the size of the input array.
