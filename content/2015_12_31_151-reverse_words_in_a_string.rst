151-reverse_words_in_a_string
#############################

:date: 2015-12-31 22:57
:tags: C, in-place string manipulation
:category: LeetCode
:slug: 151-reverse_words_in_a_string

`LeetCode Problem Link <https://leetcode.com/problems/reverse-words-in-a-string/>`_

This problem is only interesting if it's done in-place in C. In Java strings are immutable so we cannot do this
in-place.

Reversing a string in-place is very easy. Simply use two pointers ``front`` and ``back`` and then swap the
characters stored at the two pointers and then decrement ``back`` and increment ``front`` until ``back`` is
smaller than ``front``.

First modify the string such that the leading spaces and the trailing spaces are gone.

The way to do this problem is to first reverse the string and then reverse each word.

The last operation that needs to be done is to remove spaces within the string.

.. code-block:: java

  void reverseWords(char *s) {
      char *p;
      int spaces = 0;
      int length = 0;
      int i = 0;
      int j = 0;

      if (s==NULL || *s=='\0') {
        return;
      }

      p = s + strlen(s) - 1;

      while (*p == ' ') {
        *p = '\0';
        p--;
      }

      length = strlen(s);
      p = s;

      while (*p == ' ') {
        spaces++;
        p++;
      }

      for (i=0; i<length; i++) {
        s[i] = s[i+spaces];
      }

      length = length - spaces;

      reverseString(s);
      reverseEachWordInString(s);

      for (i=0; i<length; i++) {
        if (s[i] == ' ') {
          int m = 0;

          for (j=i+1; j<length; j++) {
            if (s[j] == ' ' ) {
              m++;
            }
            else {
              break;
            }
          }

          if (m > 0) {
            int z = i+1;
            for (; j<=length; j++) {
              s[z] = s[j];
              z++;
            }
            length = length - m;
          }
        }
      }
    }

    void reverseEachWordInString(char *s) {
      int i, j, k;
      int length = strlen(s);

      i=0;
      j=0;
      k=0;

      while (s[j] != '\0') {
        if (s[j] != ' ') {
          j++;
        }
        else {
          k=j-1;

          while (k > i) {
            char temp = s[k];
            s[k] = s[i];
            s[i] = temp;
            k--;
            i++;
          }
          j = j + 1;
          i = j;
          k = j;
        }
      }

      if (s[j] == '\0') {
        k=j-1;

        while (k > i) {
          char temp = s[k];
          s[k] = s[i];
          s[i] = temp;
          k--;
          i++;
        }
      }
    }

    void reverseString(char * s) {
      char *f = s;
      char *b = s + strlen(s) - 1;

      while (b >= f) {
        char temp = *f;
        *f = *b;
        *b = temp;
        f++;
        b--;
      }
    }
