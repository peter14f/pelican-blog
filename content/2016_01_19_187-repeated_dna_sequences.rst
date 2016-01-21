187-repeated_dna_sequences
##########################

:date: 2016-1-19 23:26
:tags:
:category: LeetCode
:slug: 187-repeated_dna_sequences

`LeetCode Problem Link <https://leetcode.com/problems/repeated-dna-sequences/>`_

This takes O(n) time and O(n) space.

.. code-block:: java

    public List<String> findRepeatedDnaSequences(String s) {
        List<String> ans = new ArrayList<String>();
        HashMap<String, Integer> cnt = new HashMap<String, Integer>();

        // s.length() - x = 10
        // x = s.length() - 10
        for (int i=0; i<=s.length()-10; i++) {
            String str = s.substring(i, i+10);

            if (!cnt.containsKey(str))
                cnt.put(str, 1);
            else
                cnt.put(str, cnt.get(str) + 1);
        }

        for (String str: cnt.keySet()) {
            if (cnt.get(str) > 1) {
                ans.add(str);
            }
        }

        return ans;
    }
