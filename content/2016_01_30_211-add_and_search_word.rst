211-add_and_search_word
#######################

:date: 2016-1-30 12:08
:tags: Trie, DFS
:category: LeetCode
:slug: 211-add_and_search_word

`LeetCode Problem Link <https://leetcode.com/problems/add-and-search-word-data-structure-design/>`_

Since we are told that strings contains letters from 'a' to 'z', we can should use fixed size array in
the Trie implementation. For the wildcard character searching, I just use recursion and DFS.

.. code-block:: java

    public class WordDictionary {
        class TrieNode {
            boolean isLeaf;
            TrieNode[] children;

            public TrieNode() {
                isLeaf = false;
                children = new TrieNode[26];
            }
        }

        TrieNode root;

        public WordDictionary() {
            root = new TrieNode();
        }

        // Adds a word into the data structure.
        public void addWord(String word) {
            TrieNode cur = root;

            for (int i=0; i<word.length(); i++) {
                char c = word.charAt(i);

                if (cur.children[c - 'a'] == null) {
                    cur.children[c - 'a'] = new TrieNode();
                }

                cur = cur.children[c - 'a'];
            }

            cur.isLeaf = true;
        }

        // Returns if the word is in the data structure. A word could
        // contain the dot character '.' to represent any one letter.
        public boolean search(String word) {
            TrieNode cur = root;

            for (int i=0; i<word.length(); i++) {
                char c = word.charAt(i);

                if (c == '.') {
                    return dfsCanFindAMatch(i, cur, word);
                }

                cur = cur.children[c - 'a'];

                if (cur == null)
                    return false;
            }

            return cur.isLeaf;
        }

        private boolean dfsCanFindAMatch(int i, TrieNode node, String word) {
            char c = word.charAt(i);

            if (c=='.') {
                for (char ch='a'; ch<='z'; ch++) {
                    if (node.children[ch-'a'] != null) {
                        if (i == word.length()-1) {
                            if (node.children[ch-'a'].isLeaf)
                                return true;
                        }
                        else {
                            if (dfsCanFindAMatch(i+1, node.children[ch-'a'], word))
                                return true;
                        }
                    }
                }

                return false;
            }
            else {
                node = node.children[c-'a'];

                if (node==null)
                    return false;
                else {
                    if (i == word.length() - 1)
                        return node.isLeaf;
                    else
                        return dfsCanFindAMatch(i+1, node, word);
                }
            }
        }
    }
