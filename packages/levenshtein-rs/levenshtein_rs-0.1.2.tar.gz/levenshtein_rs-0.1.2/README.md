# levenshtein_rs
Given `x: list[str]` and `y: list[str]`, this package calculates the Levenshtein distance between `a` and `b`.

## Usage
```python
from levenshtein_rs import levenshtein_list
a = "Testing one two three"
b = "one two three four"
print(levenshtein_list(a.split(), b.split()))
# 2
```
