205-isomorphic_strings
######################

:date: 2016-1-25 20:20
:tags: Hash Tables
:category: LeetCode
:slug: 205-isomorphic_strings

`LeetCode Problem Link <https://leetcode.com/problems/isomorphic-strings/>`_

We need to make sure that the mapping from character in ``t`` to character in ``s`` remains consisitent.
(Need a ``HashMap<Characte, Character>``) and that no two different characters from ``t`` map to the same
character in ``s``.

.. code-block:: java

    public boolean isIsomorphic(String s, String t) {
        HashMap<Character, Character> map = new HashMap<Character, Character>();
        HashSet<Character> mapped = new HashSet<Character>();

        for (int i=0; i<s.length(); i++) {

            char sCur = s.charAt(i);
            char tCur = t.charAt(i);
            char converted;

            if (map.containsKey(sCur)) {
                converted = map.get(sCur);
                if (converted != tCur)
                    return false;
            }
            else {
                if (mapped.contains(tCur))
                    return false;

                map.put(sCur, tCur);
                mapped.add(tCur);
            }
        }

        return true;
    }

