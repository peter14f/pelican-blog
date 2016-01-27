208-implement_trie
##################

:date: 2016-1-27 11:43
:tags: Trie, Prefix Tree
:category: LeetCode
:slug: 208-implement_trie

`LeetCode Problem Link <https://leetcode.com/problems/implement-trie-prefix-tree/>`_

I use the the null character value '\0' to mark the end of a word.

.. code-block:: java

    public class TrieNode {
        HashMap<Character, TrieNode> children;

        public TrieNode() {
            this.children = new HashMap<Character, TrieNode>();
        }

        public boolean hasChild(char c) {
            return this.children.containsKey(c);
        }

        public void insertChild(char c) {
            if (this.hasChild(c))
                return;

            if (c == '\0') {
                this.children.put(c, null);
            }

            TrieNode newChild = new TrieNode();
            this.children.put(c, newChild);
        }

        public TrieNode getChild(char c) {
            return this.children.get(c);
        }
    }


    public class Trie {
        private TrieNode root;

        public Trie() {
            root = new TrieNode();
        }

        // Inserts a word into the trie.
        public void insert(String word) {
            TrieNode cur = root;

            for (int i=0; i<word.length(); i++) {
                char c = word.charAt(i);

                if (!cur.hasChild(c)) {
                    cur.insertChild(c);
                }

                cur = cur.getChild(c);
            }

            cur.insertChild('\0');
        }

        // Returns if the word is in the trie.
        public boolean search(String word) {
            TrieNode cur = root;

            for (int i=0; i<word.length(); i++) {
                char c = word.charAt(i);

                if (!cur.hasChild(c))
                    return false;

                cur = cur.getChild(c);
            }

            return cur.hasChild('\0');
        }

        // Returns if there is any word in the trie
        // that starts with the given prefix.
        public boolean startsWith(String prefix) {
            TrieNode cur = root;

            for (int i=0; i<prefix.length(); i++) {
                char c = prefix.charAt(i);

                if (!cur.hasChild(c))
                    return false;

                cur = cur.getChild(c);
            }

            return true;
        }
    }