030-substring_with_concatenation_of_all_words
#############################################

:date: 2015-09-27 10:42
:tags: Concatenation
:category: LeetCode
:slug: 030-substring_with_concatenation_of_all_words

`LeetCode Problem Link <https://leetcode.com/problems/substring-with-concatenation-of-all-words/>`_

| Examine each and every possible substring of the desired length.
| Note that ``words`` can contain duplicates.

.. code-block:: java

    public List<Integer> findSubstring(String s, String[] words) {
        int l = words[0].length(); // length of each word in words
        int substringLen = l * words.length;
        int n = s.length();

        List<Integer> ans = new ArrayList<Integer>();

        HashMap<String, Integer> wordCnt = new HashMap<String, Integer>();

        for (int i=0; i<words.length; i++) {
            if (wordCnt.containsKey(words[i])) {
                wordCnt.put(words[i], wordCnt.get(words[i]) + 1);
            }
            else {
                wordCnt.put(words[i], 1);
            }
        }

        for (int i=0; i<n; i++) {

            if (i + substringLen > n) {
                // cannot form a substring of the desired length anymore
                break;
            }

            String substring = s.substring(i, i + substringLen);
            HashMap<String, Integer> cnt = new HashMap<String, Integer>(wordCnt);

            for (int j=0; j<substringLen; j=j+l) {
                String sSub = substring.substring(j, j+l);

                if (wordCnt.containsKey(sSub) && cnt.containsKey(sSub)) {
                    int oldCnt = cnt.get(sSub);
                    if (oldCnt == 1) {
                        cnt.remove(sSub);
                    }
                    else {
                        cnt.put(sSub, oldCnt - 1);
                    }
                }
                else {
                    break;
                }
            }

            if (cnt.isEmpty()) {
                ans.add(i);
            }

        }

        return ans;
    }