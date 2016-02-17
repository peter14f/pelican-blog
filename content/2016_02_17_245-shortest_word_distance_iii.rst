245-shortest_word_distance_iii
##############################

:date: 2016-2-17 8:36
:tags:
:category: LeetCode
:slug: 245-shortest_word_distance_iii

`LeetCode Problem Link <https://leetcode.com/problems/shortest-word-distance-iii/>`_

Pretty much the same problem as 243-shortest_word_distance. ``word1`` and ``word2`` may be the same
string now, but they represent two different strings in the input array. Still a O(n) time solution.

.. code-block:: java

    // may assume word1 and word2 are in the input string array
    // word1 and word2 may be the same and they represent two individual words in the list
    public int shortestWordDistance(String[] words, String word1, String word2) {
        int minDistance = Integer.MAX_VALUE;
        int lastSeen1 = -1;
        int lastSeen2 = -1;

        boolean same = word1.equals(word2);

        for (int i=0; i<words.length; i++) {
            if (words[i].equals(word1)) {

                if (same) {
                    if (lastSeen1 != -1) {
                        int dist = i - lastSeen1;
                        if (dist < minDistance)
                            minDistance = dist;
                    }
                }
                else {
                    if (lastSeen2 != -1) {
                        int dist = i - lastSeen2;
                        if (dist < minDistance)
                            minDistance = dist;
                    }
                }
                lastSeen1 = i;
            }
            else if (words[i].equals(word2)) {
                if (lastSeen1 != -1) {
                    int dist = i - lastSeen1;
                    if (dist < minDistance)
                        minDistance = dist;
                }
                lastSeen2 = i;
            }
        }

        return minDistance;
    }
