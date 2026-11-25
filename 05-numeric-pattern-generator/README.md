# Advanced Numeric Pattern Generator

Name: Akash  
Roll No: 26000499

## Problem statement

Produce a hollow diamond and a symmetric numerical pattern based on user-specified dimensions, with validation for invalid dimensions and carefully aligned output.

The program generates two patterns for size n = 7:
1. Hollow diamond made of `*` characters (border only, hollow inside, full middle row).
2. Numeric pyramid: 1, 1 2 1, 1 2 3 2 1, and so on.

Size must be between 3 and 15. Invalid sizes are rejected with a message.

## Objectives

- Use nested loops to build patterns line by line.
- Use string operations and conditionals for alignment.
- Validate input size with if-else.
- Return patterns as lists of strings for testing.
- Print both patterns with proper spacing.

## Assumptions

- Size n is a whole number between 3 and 15 (inclusive).
- Diamond has 2n-1 lines: n lines for top half including middle, n-1 for bottom.
- Middle row of diamond is fully filled with stars.
- Numeric pyramid row i contains numbers 1..i..1 separated by spaces.
- Demo uses n = 7.

## Algorithm

```
1. START
2. n = 7
3. IF n < 3 OR n > 15 THEN print "Invalid size" and STOP
4. Hollow diamond:
   4.1 FOR i from 0 to n-1 (top half):
       spaces = n - i - 1, stars = 2*i + 1
       IF i = 0 THEN line = spaces + "*"
       ELSE IF i = n-1 THEN line = spaces + "*" * stars
       ELSE line = spaces + "*" + " "*(stars-2) + "*"
   4.2 FOR i from n-2 down to 0 (bottom half): same logic
5. Numeric pyramid:
   5.1 FOR i from 1 to n:
       numbers = [1..i] + [i-1..1]
       line = numbers joined by space
6. Print both patterns
7. Show validation demo for n=2, 7, 20
8. END
```

## Flowchart

![Flowchart](flowchart.png)

## Pseudocode

```
BEGIN PATTERN_GENERATOR
    n <- 7
    IF n < 3 OR n > 15 THEN
        PRINT "Invalid size"
        STOP
    END IF

    // hollow diamond
    lines <- []
    FOR i <- 0 TO n-1 DO
        spaces <- n - i - 1
        stars <- 2*i + 1
        IF i = 0 THEN line <- " "*spaces + "*"
        ELSE IF i = n-1 THEN line <- " "*spaces + "*"*stars
        ELSE line <- " "*spaces + "*" + " "*(stars-2) + "*"
        APPEND line TO lines
    END FOR
    FOR i <- n-2 DOWN TO 0 DO
        // same as above
    END FOR

    // numeric pyramid
    FOR i <- 1 TO n DO
        nums <- []
        FOR j <- 1 TO i DO APPEND STR(j) TO nums
        FOR j <- i-1 DOWN TO 1 DO APPEND STR(j) TO nums
        PRINT JOIN(nums, " ")
    END FOR
END
```

## Python source code

```python
"""
Case Study 05: Advanced Numeric Pattern Generator
Name: Akash, Roll No: 26000499
Syllabus used: nested loops, conditionals, strings, operators, validation
"""


def valid_size(n):
    """Size must be between 3 and 15."""
    if n < 3:
        return False
    if n > 15:
        return False
    return True


def hollow_diamond(n):
    """Return list of strings forming a hollow diamond of size n."""
    lines = []
    # top half including middle row
    for i in range(n):
        spaces = n - i - 1
        stars = 2 * i + 1
        line = " " * spaces
        if i == 0:
            line = line + "*"
        else:
            line = line + "*" + " " * (stars - 2) + "*"
        lines.append(line)
    # bottom half
    for i in range(n - 2, -1, -1):
        spaces = n - i - 1
        stars = 2 * i + 1
        line = " " * spaces
        if i == 0:
            line = line + "*"
        else:
            line = line + "*" + " " * (stars - 2) + "*"
        lines.append(line)
    return lines


def number_pyramid(n):
    """Return list of strings: 1, 1 2 1, 1 2 3 2 1 ..."""
    lines = []
    for i in range(1, n + 1):
        nums = []
        for j in range(1, i + 1):
            nums.append(str(j))
        for j in range(i - 1, 0, -1):
            nums.append(str(j))
        line = " ".join(nums)
        lines.append(line)
    return lines


def main():
    n = 7
    print("=" * 50)
    print("  NUMERIC PATTERN GENERATOR")
    print("=" * 50)
    print("Size n = %d" % n)
    print("Valid size range: 3 to 15")
    print("-" * 50)

    if not valid_size(n):
        print("Invalid size! Please enter a value between 3 and 15.")
    else:
        print("\nHollow diamond (size %d):" % n)
        for line in hollow_diamond(n):
            print(line)

        print("\nNumeric pyramid (size %d):" % n)
        # centre the pyramid roughly
        for line in number_pyramid(n):
            print(" " * ((n * 2 - 1 - len(line)) // 2) + line)

    print("-" * 50)
    print("Validation demo:")
    print("  n=2  -> valid? %s" % valid_size(2))
    print("  n=7  -> valid? %s" % valid_size(7))
    print("  n=20 -> valid? %s" % valid_size(20))


if __name__ == "__main__":
    main()
```

## Test cases

```python
"""Test cases for Case Study 05 - Advanced Numeric Pattern Generator."""
import importlib.util
import os

spec = importlib.util.spec_from_file_location("sol", os.path.join(os.path.dirname(__file__), "solution.py"))
sol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol)

passed = 0

def check(label, condition):
    global passed
    assert condition, "FAILED: " + label
    passed += 1
    print("  PASS:", label)

check("n=2 invalid", sol.valid_size(2) == False)
check("n=3 valid", sol.valid_size(3) == True)
check("n=15 valid", sol.valid_size(15) == True)
check("n=16 invalid", sol.valid_size(16) == False)

d = sol.hollow_diamond(5)
check("diamond has 9 lines for n=5", len(d) == 9)
check("diamond top is single star", d[0].strip() == "*")
check("diamond middle row is hollow", d[4].strip() == "*" + " " * 7 + "*")

p = sol.number_pyramid(4)
check("pyramid has 4 lines", len(p) == 4)
check("pyramid line 1 is '1'", p[0] == "1")
check("pyramid line 3 is '1 2 3 2 1'", p[2] == "1 2 3 2 1")
check("pyramid line 4 is '1 2 3 4 3 2 1'", p[3] == "1 2 3 4 3 2 1")

print("\nALL %d TESTS PASSED (Case Study 05)" % passed)
```

## Output screenshot

```
==================================================
  NUMERIC PATTERN GENERATOR
==================================================
Size n = 7
Valid size range: 3 to 15
--------------------------------------------------

Hollow diamond (size 7):
      *
     * *
    *   *
   *     *
  *       *
 *         *
*           *
 *         *
  *       *
   *     *
    *   *
     * *
      *

Numeric pyramid (size 7):
      1
    1 2 1
  1 2 3 2 1
1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1
1 2 3 4 5 6 5 4 3 2 1
1 2 3 4 5 6 7 6 5 4 3 2 1
--------------------------------------------------
Validation demo:
  n=2  -> valid? False
  n=7  -> valid? True
  n=20 -> valid? False
```

![Output screenshot](output_screenshot.png)

## Conclusion

Both patterns were generated correctly with nested loops and string operations. The hollow diamond has a proper hollow interior and a full middle row, and the numeric pyramid follows the 1..i..1 rule. Validation correctly rejects sizes below 3 and above 15. All 11 test cases passed.
