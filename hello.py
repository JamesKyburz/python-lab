#!/usr/bin/env python3

import re
import sys

items = [0, 3, 2, 1, 4, 5]
items.sort()

even = [x for x in items if x % 2 == 0]

print(even)

print([x for x in filter(lambda x: x % 2 == 0, range(5))])

with open(__file__, "r") as f:
    for line in f.readlines():
        print(line, end="")

with open(__file__, "r") as f:
    lines = [line for line in f.readlines() if re.match(r"^print", line)]
    print("line count with start with print is %d" % len(lines))


def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


for x in infinite_sequence():
    if x < 10:
        print(x)
    else:
        break

set_of_things = {"a", "a", "b", "c"}

print(set_of_things, "size is", len(set_of_things), type(set_of_things))

try:
    x = int("crash")
except Exception as err:
    print("error {0}".format(err), type(err))
finally:
    print("finally!")

print("format 3 values {0}, {1}, and {2}".format(1, 2, 3))

x = {"key1": "value1 from x", "key2": "value2 from x"}
y = {"key2": "value2 from y", "key3": "value3 from y"}
x_or_y = x | y

print("x", x)
print("y", y)
print("x_or_y", x_or_y)

print("all ok")
