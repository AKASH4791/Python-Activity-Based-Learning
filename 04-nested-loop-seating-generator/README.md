# Case Study 04 — Nested Loop Examination Seating Generator

**Name:** Akash  
**Roll No:** 26000499  
**Subject:** Python Programming — Activity-Based Learning

## 1. Problem Statement

Generate a seating arrangement with row and column identifiers, reserved positions, and fixed classroom capacity.

The hall has 4 rows and 6 columns (24 seats). Some seats are reserved and must be shown as "RES". Remaining seats are filled with roll numbers starting from 101. The program should also check if the hall has enough seats for 20 students.

## 2. Objectives

- Use nested loops to generate rows and columns.
- Store reserved positions as a list of tuples.
- Use tuple unpacking to check reserved seats.
- Build a 2D grid using nested lists.
- Print the arrangement with row/column headers and capacity check.

## 3. Assumptions

- Rows = 4, Columns = 6, total seats = 24.
- Reserved seats are (1,2), (2,5), (3,3), (4,1), (4,6) — 5 seats.
- Roll numbers start from 101 and increase by 1 for each available seat.
- Reserved seats stay empty for invigilator / late students.

## 4. Algorithm

```
1. START
2. Set ROWS=4, COLS=6, RESERVED list of tuples, START_ROLL=101
3. Create empty grid
4. FOR r from 1 to ROWS:
   4.1 Create empty row list
   4.2 FOR c from 1 to COLS:
       4.2.1 IF (r,c) is in RESERVED THEN append "RES"
       4.2.2 ELSE append current roll number as string, roll += 1
   4.3 Append row to grid
5. Print grid with column numbers on top and R1, R2... on side
6. Print reserved positions
7. available = ROWS*COLS - len(RESERVED)
8. IF available >= 20 THEN print OK ELSE print WARNING
9. END
```

## 5. Flowchart

![Flowchart](flowchart.png)

*Figure: Flowchart for this case study (Start/End = oval, Process = rectangle, Decision = diamond, Input/Output = parallelogram). Text version below:*

```
                    +---------+
                    |  START  |
                    +----┬----+
                         v
              +----------------------+
              | ROWS=4, COLS=6       |
              | RESERVED=[...]       |
              +----------+-----------+
                         v
              +----------------------+
              | grid = []            |
              +----------+-----------+
                         v
          +-------------------------+<-----------+
          | FOR r = 1 to ROWS    |            |
          +-----------+-------------+            |
                      v                          |
          +-------------------------+<-----------+
          | FOR c = 1 to COLS    |            |
          +-----------+-------------+            |
                      v                          |
          +----------------------+               |
          | (r,c) reserved ?     |--YES--> "RES"
          +-----------+----------+               |
                      NO                         |
                      v                          |
          +----------------------+               |
          | add roll, roll += 1  |---------------+
          +-----------+----------+
                      v
          +----------------------+
          | print grid, capacity |
          +----------+-----------+
                     v
                  +---------+
                  |   END   |
                  +---------+
```

## 6. Pseudocode

```
BEGIN SEATING_GENERATOR
    ROWS <- 4, COLS <- 6
    RESERVED <- [(1,2),(2,5),(3,3),(4,1),(4,6)]
    roll <- 101
    grid <- []

    FOR r <- 1 TO ROWS DO
        row <- []
        FOR c <- 1 TO COLS DO
            reserved <- False
            FOR each (rr, cc) IN RESERVED DO
                IF rr = r AND cc = c THEN reserved <- True
            END FOR
            IF reserved THEN
                APPEND "RES" TO row
            ELSE
                APPEND STR(roll) TO row
                roll <- roll + 1
            END IF
        END FOR
        APPEND row TO grid
    END FOR

    PRINT grid with headers
    available <- ROWS * COLS - LENGTH(RESERVED)
    IF available >= 20 THEN PRINT "OK" ELSE PRINT "WARNING"
END
```

## 7. Python Source Code

Full program: [`solution.py`](./solution.py)

```python
def is_reserved(r, c):
    for rr, cc in RESERVED:  # tuple unpacking
        if rr == r and cc == c:
            return True
    return False

def generate():
    grid = []
    roll = START_ROLL
    for r in range(1, ROWS + 1):
        row = []
        for c in range(1, COLS + 1):
            if is_reserved(r, c):
                row.append("RES")
            else:
                row.append(str(roll))
                roll = roll + 1
        grid.append(row)
    return grid
```

Run with: `python3 solution.py`

## 8. Test Cases

Test file: [`test_cases.py`](./test_cases.py) — 9 tests, all passing.

| ID | Input | Expected | Result |
|----|-------|----------|--------|
| TC-01 | is_reserved(1,2) | True | True — PASS |
| TC-02 | is_reserved(1,1) | False | False — PASS |
| TC-03 | is_reserved(4,6) | True | True — PASS |
| TC-04 | Grid size | 4 rows | 4 — PASS |
| TC-05 | Columns per row | 6 | 6 — PASS |
| TC-06 | grid[0][1] | "RES" | "RES" — PASS |
| TC-07 | grid[0][0] | "101" | "101" — PASS |
| TC-08 | Count of RES cells | 5 | 5 — PASS |
| TC-09 | Unique roll numbers | 19 unique | 19 — PASS |

## 9. Output

![Output screenshot](output_screenshot.png)

Full output: [`output.txt`](./output.txt)

```
          1     2     3     4     5     6
R1     101   RES   102   103   104   105
R2     106   107   108   109   RES   110
R3     111   112   RES   113   114   115
R4     RES   116   117   118   119   RES

Capacity check:
  WARNING: only 19 seats available, not enough for 20 students.
```

## 10. Conclusion

Nested loops worked well for generating the seating grid. Reserved seats were correctly skipped and roll numbers were assigned in order. The hall has 19 available seats, so it is not enough for 20 students — the program correctly shows a warning. All 9 test cases passed.
