#!/usr/bin/env python3
from editdistance import eval
import random
import time

random.seed(42)
lyst1 = [random.choice(["a", "b"]) for _ in range(7000)]
lyst2 = [random.choice(["a", "b"]) for _ in range(7000)]

start = time.time()
print("Using eval")
print(eval(lyst1, lyst2))
print(time.time() - start)
