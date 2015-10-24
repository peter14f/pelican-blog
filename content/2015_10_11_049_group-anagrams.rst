049_group-anagrams
##################

:date: 2015-10-11 18:16
:tags: Anagrams
:category: LeetCode
:slug: 049_group-anagrams

`LeetCode Problem Link <https://leetcode.com/problems/anagrams/>`_

This problem just tests to see if you can lump all the anagrams together. If two words are anagrams, their sorted
versions must be the same. OJ wants words within each inner list to be sorted lexicographically. The easiest way
to achieve this is to sort the input string array at the very beginning.

.. code-block:: java

    public List<List<String>> groupAnagrams(String[] strs) {

        /* we sort the input array right away because OJ requires that the
         * inner lists be in lexicographical order
         */
        Arrays.sort(strs);

        HashMap<String, List<String>> anagrams = new HashMap<String, List<String>>();
        List<List<String>> ans = new ArrayList<List<String>>();

        for (int i=0; i<strs.length; i++) {
            char[] s_arr = strs[i].toCharArray();
            Arrays.sort(s_arr);
            String key = new String(s_arr);

            if (anagrams.containsKey(key)) {
                anagrams.get(key).add(strs[i]);
            }
            else {
                List<String> list = new ArrayList<String>();
                list.add(strs[i]);
                anagrams.put(key, list);
            }
        }

        for (List<String> list : anagrams.values()) {
            ans.add(list);
        }

        return ans;
    }