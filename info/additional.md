**Rank 2**:
 
In default pattern level (level = 1) we using binary form.
If the patter level equals 2, then convert the integer pattern into ternary numeral system (base 3).
**0 is a digit, 1 is a lowercase letter, 2 is an uppercase letter.**

_Precondition rank 2:_

```python
re.match(structure, "\A[a-zA-Z0-9]{1, 32}\Z")
pattern_level in (1, 2)
```


**Rank 3**: If the pattern level equals 3, then convert the integer pattern into
Quaternary numeral system (base 4). 
**0 is a digit, 1 is a lowercase letter, 2 is an uppercase letter, 3 is a whitespace.**

_Precondition rank 3:_

```python
re.match(structure, "\A[ a-zA-Z0-9]{1, 32}\Z")
pattern_level in (1, 2, 3)
```