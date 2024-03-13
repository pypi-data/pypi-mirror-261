#!/usr/bin/env python3
from levenshtein_rs import levenshtein_list

a = "Testing one two three"
b = "one two three four"
print(levenshtein_list(a.split(), b.split()))
