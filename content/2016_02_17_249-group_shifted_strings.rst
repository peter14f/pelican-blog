249-group_shifted_strings
#########################

:date: 2016-2-17 21:56
:tags:
:category: LeetCode
:slug: 249-group_shifted_strings

`LeetCode Problem Link <https://leetcode.com/problems/group-shifted-strings/>`_

The distance between consecutive characters in a string may not be constant.
Take "cno" as an example. 'n' - 'c' = 11 but 'o' - 'n' = 1.

If we transform each string such that the first character is 'a' while maintaining the distance between consecutive
characters, we get a signature of the string. If two strings have the same signature, then they just be in the same
group. This idea is very similar to how we can find out if two strings are anagrams.

.. code-block:: java

    public List<List<String>> groupStrings(String[] strings) {

        HashMap<String, List<String>> signatures = new HashMap<String, List<String>>();
        List<List<String>> groups = new ArrayList<List<String>>();

        for (int i=0; i<strings.length; i++) {
            String signature = getSignature(strings[i]);

            if (!signatures.containsKey(signature)) {
                List<String> newList = new ArrayList<String>();
                signatures.put(signature, newList);
            }
            signatures.get(signature).add(strings[i]);
        }

        for (List<String> l: signatures.values()) {
            Collections.sort(l);
            groups.add(l);
        }

        return groups;
    }

    private String getSignature(String s) {

        if (s.length() == 0)
            return s;

        char c1 = s.charAt(0);

        char diff = (char) (c1 - 'a');
        StringBuffer sb = new StringBuffer();

        for (int i=0; i<s.length(); i++) {
            char c = s.charAt(i);

            char newC = (char) (c - diff);

            if (newC < 'a') {
                newC += 26;
            }

            sb.append(newC);
        }

        return sb.toString();
    }

