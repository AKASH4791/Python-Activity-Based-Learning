# Case Study 07 — Text Compression Using Character Runs

**Name:** Akash  
**Roll No:** 26000499  
**Subject:** Python Programming — Activity-Based Learning

## 1. Problem Statement

Encode a string by grouping consecutive repeated characters (run-length encoding) and compare original and encoded lengths, including cases where encoding is not beneficial.

Example: `aaabbbcc` becomes `a3b3c2`. Single characters with count 1 stay as-is (e.g. `abc` stays `abc`). The program also decodes back to verify correctness.

## 2. Objectives

- Traverse a string with a loop and count consecutive repeats.
- Build encoded string using string concatenation.
- Compare original length vs encoded length.
- Implement decoding to verify round-trip correctness.
- Show cases where compression helps and where it does not.

## 3. Assumptions

- Input strings contain only lowercase letters (no digits), so digits in encoded form are unambiguous.
- Count is written as a decimal number after the character (e.g. a3 means three a's).
- If count is 1, only the character is written, not "a1".
- 7 sample strings are used.

## 4. Algorithm

```
1. START
2. FOR each string s in SAMPLES:
   2.1 result = "", count = 1
   2.2 FOR i from 1 to len(s)-1:
       IF s[i] = s[i-1] THEN count += 1
       ELSE:
           IF count = 1 THEN result += s[i-1]
           ELSE result += s[i-1] + str(count)
           count = 1
   2.3 Handle last run similarly
   2.4 encoded = result
   2.5 Print original, encoded, lengths, useful? (len(encoded) < len(s))
3. Decode check: FOR each s, decode(compress(s)) should equal s
4. END
```

Decode algorithm:
```
1. result = "", i = 0
2. WHILE i < len(s):
   ch = s[i], i += 1
   num = ""
   WHILE i < len(s) AND s[i] is digit: num += s[i], i += 1
   IF num = "" THEN result += ch
   ELSE result += ch repeated int(num) times
3. Return result
```

## 5. Flowchart

```
                    +---------+
                    |  START  |
                    +----┬----+
                         v
              +----------------------+
              | FOR each string s    |
              +----------+-----------+
                         v
              +----------------------+
              | count = 1            |
              | FOR i=1 to len-1     |
              |   s[i]=s[i-1] ?      |--YES--> count += 1
              +----------+-----------+--NO--> write char+count
                         v                     count=1
              +----------------------+
              | write last run       |
              +----------+-----------+
                         v
              +----------------------+
              | compare lengths      |
              | decode and verify    |
              +----------+-----------+
                         v
                  +---------+
                  |   END   |
                  +---------+
```

## 6. Pseudocode

```
BEGIN RLE_COMPRESSION
    FOR each s IN SAMPLES DO
        result <- ""
        count <- 1
        FOR i <- 1 TO LENGTH(s)-1 DO
            IF s[i] = s[i-1] THEN
                count <- count + 1
            ELSE
                IF count = 1 THEN result <- result + s[i-1]
                ELSE result <- result + s[i-1] + STR(count)
                count <- 1
            END IF
        END FOR
        IF count = 1 THEN result <- result + s[LENGTH(s)-1]
        ELSE result <- result + s[LENGTH(s)-1] + STR(count)
        PRINT s, result, LENGTH(s), LENGTH(result)
    END FOR
    // decode check
    FOR each s IN SAMPLES DO
        IF DECODE(ENCODE(s)) = s THEN PRINT "OK" ELSE PRINT "MISMATCH"
    END FOR
END
```

## 7. Python Source Code

Full program: [`solution.py`](./solution.py)

```python
def compress(s):
    if len(s) == 0:
        return ""
    result = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count = count + 1
        else:
            if count == 1:
                result = result + s[i - 1]
            else:
                result = result + s[i - 1] + str(count)
            count = 1
    if count == 1:
        result = result + s[len(s) - 1]
    else:
        result = result + s[len(s) - 1] + str(count)
    return result
```

Run with: `python3 solution.py`

## 8. Test Cases

Test file: [`test_cases.py`](./test_cases.py) — 9 tests, all passing.

| ID | Input | Expected | Result |
|----|-------|----------|--------|
| TC-01 | "aaabbbcc" | "a3b3c2" | "a3b3c2" — PASS |
| TC-02 | "abc" | "abc" | "abc" — PASS |
| TC-03 | "aaaa" | "a4" | "a4" — PASS |
| TC-04 | "" | "" | "" — PASS |
| TC-05 | "x" | "x" | "x" — PASS |
| TC-06 | "mississippi" roundtrip | same string | OK — PASS |
| TC-07 | "aaabaaa" roundtrip | same string | OK — PASS |
| TC-08 | "aabbaabb" | "a2b2a2b2" | "a2b2a2b2" — PASS |
| TC-09 | "hello" | "hel2o" | "hel2o" — PASS |

## 9. Output

![Output screenshot](output_screenshot.png)

Full output: [`output.txt`](./output.txt)

```
Original       Encoded        Orig len  Enc len  Useful?
aaabbbcc       a3b3c2                8        6  yes
abc            abc                   3        3  no
aaaa           a4                    4        2  yes
mississippi    mis2is2ip2i          11       11  no
```

## 10. Conclusion

Run-length encoding works well when there are many repeats (e.g. `aaaa` becomes `a4`), but it does not help for strings without repeats like `abc`. The decode check confirmed that every encoded string converts back to the original. All 9 test cases passed.
