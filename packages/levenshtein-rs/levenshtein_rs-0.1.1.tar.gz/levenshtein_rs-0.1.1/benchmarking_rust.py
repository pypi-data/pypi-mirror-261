#!/usr/bin/env python3
from levenshtein_rs import levenshtein_list
import random
import time

random.seed(42)
lyst1 = [random.choice(["a", "b"]) for _ in range(7000)]
lyst2 = [random.choice(["a", "b"]) for _ in range(7000)]

start = time.time()
print("Using levenshtein_list")
print(levenshtein_list(lyst1, lyst2))
print(time.time() - start)
