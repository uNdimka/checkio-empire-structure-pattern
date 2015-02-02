You are given a pattern as a positive integer and a row structure as a word.
For the comparison, the recognize system should convert the integer pattern into binary form,
append zeros to left for the structure length and compare this combination with the structure.

**1 is a letter. 0 is a digit.**

If the pattern and the structure are coincided, then return True, else -- False.
If pattern is longer than a structure, then they are not coincided (For example - 8 = 1000 and "a").

For example. The pattern is 42 and the structure is "12a0b3e4".
42 == 101010 in binary form, but this is not enough of length. Let's append zeroes -- "00101010".
Then compare:

```
      42 == 00101010
12a0b3e4 == DDLDLDLD
--------------------
    True    VVVVVVVV
```

One more example -- 101 and "ab23b4zz":

```
     101 == 01100101
ab23b4zz == LLDDLDLL
--------------------
   False    XVXVXXXV
```