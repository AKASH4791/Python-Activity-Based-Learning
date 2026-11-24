# Case Study 01 — University Scholarship Allocation

**Name:** Akash  
**Roll No:** 26000499  
**Subject:** Python Programming — Activity-Based Learning

## 1. Problem Statement

Design a system that evaluates university scholarship applicants using aggregate marks, subject-wise minimum scores, attendance, and family income criteria, ranks the eligible students, and resolves ties using predefined rules.

Each applicant record is given as a tuple `(roll, name, marks list, attendance %, income)`. The program must:

1. Reject an applicant if aggregate is below 60, or any subject mark is below 50, or attendance is below 75%, or family income is above Rs 5,00,000.
2. Rank all eligible applicants by aggregate in descending order.
3. Resolve ties by higher attendance first, then lower income, then roll number.
4. Show every rejected applicant with the exact reason(s).

## 2. Objectives

- Store applicant records using tuples and lists.
- Use conditional statements for multi-criteria eligibility checking.
- Calculate aggregate using operators and loops.
- Rank data with a tie-breaking rule.
- Use tuple unpacking to read records.
- Print a formatted report of eligible and rejected students.

## 3. Assumptions

- Every applicant has 5 subject marks out of 100.
- Aggregate means average of the 5 marks.
- Income limit is Rs 5,00,000, attendance limit is 75%, subject minimum is 50.
- All data used is sample/hypothetical data for testing.
- Tie-breaking order is fixed: attendance high to low, income low to high, roll low to high.

## 4. Algorithm

```
1. START
2. Set MIN_AGGREGATE=60, MIN_SUBJECT=50, MIN_ATTENDANCE=75, MAX_INCOME=500000
3. Create empty lists eligible and rejected
4. FOR each applicant in APPLICANTS:
   4.1 Unpack applicant into roll, name, marks, attendance, income
   4.2 Calculate aggregate = sum of marks / number of marks
   4.3 Create empty reasons list
   4.4 IF aggregate < 60 THEN add reason
   4.5 FOR each subject mark: IF mark < 50 THEN add reason with subject name
   4.6 IF attendance < 75 THEN add reason
   4.7 IF income > 500000 THEN add reason
   4.8 IF reasons is empty THEN add to eligible ELSE add to rejected
5. Sort eligible by (-aggregate, -attendance, income, roll)
6. Print ranked table
7. Check adjacent rows for equal aggregate and print tie-resolution note
8. Print rejected applicants with reasons
9. Print summary counts
10. END
```

## 5. Flowchart

```
                    +---------+
                    |  START  |
                    +----┬----+
                         v
              +----------------------+
              | read policy limits &  |
              | applicant records     |
              +----------+-----------+
                         v
             +----------------------+
             | eligible=[] rejected=[]|
             +----------+------------+
                        v
          +-------------------------+<-----------+
          | FOR each applicant      |            |
          +-----------+-------------+            |
                      v                          |
          +----------------------+               |
          | UNPACK tuple         |               |
          | roll,name,marks,att  |               |
          +-----------+----------+               |
                      v                          |
          +----------------------+               |
          | aggregate = sum/n    |               |
          | reasons = []         |               |
          +-----------+----------+               |
                      v                          |
   +----------------------------------+          |
   | aggregate>=60 AND all marks>=50  |--NO--> reject
   | AND att>=75 AND income<=500000 ? |   +reasons
   +----------------+-----------------+          |
                    YES v                        |
          +----------------------+               |
          | add to eligible      |---------------+
          +-----------+----------+
                      v
          +----------------------+
          | SORT by aggregate,   |
          | attendance, income   |
          +----------+-----------+
                     v
          +----------------------+
          | print table, ties,   |
          | rejections, summary  |
          +----------+-----------+
                     v
                  +---------+
                  |   END   |
                  +---------+
```

## 6. Pseudocode

```
BEGIN SCHOLARSHIP_ALLOCATION
    MIN_AGGREGATE <- 60
    MIN_SUBJECT <- 50
    MIN_ATTEND <- 75
    MAX_INCOME <- 500000
    SUBJECTS <- ["Maths","Physics","Chemistry","English","CS"]

    FOR each applicant IN APPLICANTS DO
        (roll, name, marks, attendance, income) <- applicant
        aggregate <- SUM(marks) / LENGTH(marks)
        reasons <- []

        IF aggregate < MIN_AGGREGATE THEN
            APPEND "aggregate too low" TO reasons
        FOR i <- 0 TO LENGTH(marks)-1 DO
            IF marks[i] < MIN_SUBJECT THEN
                APPEND SUBJECTS[i] + " below minimum" TO reasons
        END FOR
        IF attendance < MIN_ATTEND THEN APPEND "attendance low" TO reasons
        IF income > MAX_INCOME THEN APPEND "income above limit" TO reasons

        IF LENGTH(reasons) = 0 THEN
            APPEND (roll, name, aggregate, attendance, income) TO eligible
        ELSE
            APPEND (roll, name, reasons) TO rejected
    END FOR

    SORT eligible BY (-aggregate, -attendance, income, roll)
    PRINT ranked list
    CHECK ties and print explanation
    PRINT rejected list with reasons
    PRINT summary
END
```

## 7. Python Source Code

Full program: [`solution.py`](./solution.py)

Main logic:

```python
def check_eligibility(applicant):
    roll, name, marks, attendance, income = applicant  # tuple unpacking
    total = 0
    for m in marks:
        total = total + m
    aggregate = total / len(marks)
    reasons = []
    if aggregate < MIN_AGGREGATE:
        reasons.append("aggregate %.1f below %.0f" % (aggregate, MIN_AGGREGATE))
    for i in range(len(marks)):
        if marks[i] < MIN_SUBJECT:
            reasons.append("%s score %d below %d" % (SUBJECTS[i], marks[i], MIN_SUBJECT))
    if attendance < MIN_ATTENDANCE:
        reasons.append("attendance %.1f%% below %.0f%%" % (attendance, MIN_ATTENDANCE))
    if income > MAX_INCOME:
        reasons.append("family income %d above limit %d" % (income, MAX_INCOME))
    return len(reasons) == 0, aggregate, reasons

def rank_key(record):
    roll, name, aggregate, attendance, income = record
    return (-aggregate, -attendance, income, roll)
```

Run with: `python3 solution.py`

## 8. Test Cases

Test file: [`test_cases.py`](./test_cases.py) — 8 tests, all passing.

| ID | Input | Expected | Result |
|----|-------|----------|--------|
| TC-01 | S101 Ananya [82,76,90,71,85], 92%, 320000 | eligible, aggregate 80.8 | eligible, 80.80 — PASS |
| TC-02 | S102 Bharat [55,48,62,70,58] | rejected, aggregate 58.6 | rejected, 58.6 — PASS |
| TC-03 | S102 Physics = 48 | subject violation reported | "Physics score 48 below 50" — PASS |
| TC-04 | S103 income 610000 | income violation | "family income 610000 above limit" — PASS |
| TC-05 | S106 attendance 71% | attendance violation | "attendance 71.0% below 75%" — PASS |
| TC-06 | Rank all eligible | highest aggregate first | S105 (91.20) ranked #1 — PASS |
| TC-07 | S108 vs S104 both 61.40 | tie broken by attendance | S108 (88%) above S104 (76%) — PASS |
| TC-08 | All 8 applicants | 4 eligible / 4 rejected | 4 / 4 — PASS |

## 9. Output

![Output screenshot](output_screenshot.png)

Full output: [`output.txt`](./output.txt)

```
Rank  Roll      Name       Aggregate   Attendance
1     S105      Fatima     91.20       97.0%
2     S101      Ananya     80.80       92.0%
3     S108      Ishaan     61.40       88.0%
4     S104      Deepak     61.40       76.0%

TIE RESOLUTION LOG:
  Tie at aggregate 61.40 between S108 and S104 -> broken by attendance
  (88% vs 76%), higher attendance ranked first.
```

## 10. Conclusion

I implemented the scholarship allocation system using only tuples, lists, loops, conditionals and tuple unpacking. The program correctly screens applicants on four criteria and ranks them with a clear tie-breaking rule. In the sample data, 4 students were eligible and 4 were rejected, and the tie at 61.40 was resolved by attendance as expected. All 8 test cases passed, so the logic is working correctly.
