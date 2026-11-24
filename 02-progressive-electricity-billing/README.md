# Case Study 02 — Progressive Electricity Billing

**Name:** Akash  
**Roll No:** 26000499  
**Subject:** Python Programming — Activity-Based Learning

## 1. Problem Statement

Calculate household electricity bills using multiple consumption slabs, fixed charges, surcharges (cess), and rebates, then compare bills across several months and identify unusual increases.

Slab rates used in this program:
- 0–100 units: Rs 5 per unit
- 101–300 units: Rs 7 per unit
- 301–500 units: Rs 9 per unit
- Above 500 units: Rs 12 per unit

Fixed charge is Rs 50 per month. A 2% education cess is added on the energy charge. If consumption decreases compared to the previous month, a 5% rebate is given on the energy charge. A month-on-month increase above 30% is flagged as unusual.

## 2. Objectives

- Calculate slab-wise energy charge using loops and tuples.
- Apply fixed charge, cess and rebate using operators and conditionals.
- Compare monthly consumption and detect unusual increases.
- Store monthly data in lists of tuples and use tuple unpacking.
- Print a formatted bill statement.

## 3. Assumptions

- Consumption is measured in units (kWh) and is always a whole number.
- First month has no previous month, so no rebate is applied.
- Rebate is applied only when current units are less than previous month units.
- Unusual increase means more than 30% rise in units compared to previous month.
- All consumption values are sample data.

## 4. Algorithm

```
1. START
2. Define SLABS as list of (limit, rate) tuples
3. Set FIXED_CHARGE=50, CESS_RATE=0.02, REBATE_RATE=0.05
4. FOR each (month, units) in MONTHS:
   4.1 Calculate energy charge slab by slab:
       remaining = units, lower = 0, charge = 0
       FOR each (limit, rate) in SLABS:
           units_in_slab = min(remaining, limit - lower)
           charge += units_in_slab * rate
           remaining -= units_in_slab, lower = limit
   4.2 cess = energy * 0.02
   4.3 IF prev_units is not None AND units < prev_units THEN rebate = energy * 0.05 ELSE rebate = 0
   4.4 total = energy + fixed + cess - rebate
   4.5 Store bill and update prev_units = units
5. Print bill table
6. FOR i from 1 to len(bills)-1:
   change = (units[i] - units[i-1]) / units[i-1]
   IF change > 0.30 THEN flag "UNUSUAL INCREASE"
   ELSE IF change < 0 THEN note "rebate applied"
7. Find highest and lowest bill
8. END
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
              | read slabs, months   |
              +----------+-----------+
                         v
              +----------------------+
              | prev = None          |
              +----------+-----------+
                         v
          +-------------------------+<-----------+
          | FOR each month, units|            |
          +-----------+-------------+            |
                      v                          |
          +----------------------+               |
          | calculate slab charge|               |
          | cess, rebate, total  |               |
          +-----------+----------+               |
                      v                          |
          +----------------------+               |
          | store bill, prev=units|--------------+
          +-----------+----------+
                      v
          +----------------------+
          | print bill table     |
          +----------+-----------+
                     v
          +----------------------+
          | compare month to     |
          | month, flag >30%     |
          +----------+-----------+
                     v
          +----------------------+
          | highest / lowest bill|
          +----------+-----------+
                     v
                  +---------+
                  |   END   |
                  +---------+
```

## 6. Pseudocode

```
BEGIN ELECTRICITY_BILLING
    SLABS <- [(100,5.0),(300,7.0),(500,9.0),(1000000,12.0)]
    FIXED <- 50, CESS <- 0.02, REBATE <- 0.05
    prev <- None

    FOR each (month, units) IN MONTHS DO
        remaining <- units, lower <- 0, energy <- 0
        FOR each (limit, rate) IN SLABS DO
            slab_units <- MIN(remaining, limit - lower)
            energy <- energy + slab_units * rate
            remaining <- remaining - slab_units
            lower <- limit
            IF remaining <= 0 THEN EXIT LOOP
        END FOR
        cess <- energy * CESS
        IF prev IS NOT None AND units < prev THEN
            rebate <- energy * REBATE
        ELSE
            rebate <- 0
        total <- energy + FIXED + cess - rebate
        STORE (month, units, energy, cess, rebate, total)
        prev <- units
    END FOR

    PRINT bill table
    FOR i <- 1 TO LENGTH(bills)-1 DO
        change <- (units[i] - units[i-1]) / units[i-1]
        IF change > 0.30 THEN PRINT "UNUSUAL INCREASE"
    END FOR
    FIND highest and lowest bill
END
```

## 7. Python Source Code

Full program: [`solution.py`](./solution.py)

Key functions:

```python
def slab_charge(units):
    remaining = units
    lower = 0
    charge = 0.0
    for limit, rate in SLABS:  # tuple unpacking
        if remaining <= 0:
            break
        slab_units = remaining
        if slab_units > limit - lower:
            slab_units = limit - lower
        charge = charge + slab_units * rate
        remaining = remaining - slab_units
        lower = limit
    return charge

def compute_bill(units, prev_units):
    energy = slab_charge(units)
    cess = energy * CESS_RATE
    rebate = 0.0
    if prev_units is not None and units < prev_units:
        rebate = energy * REBATE_RATE
    total = energy + FIXED_CHARGE + cess - rebate
    return round(energy, 2), round(cess, 2), round(rebate, 2), round(total, 2)
```

Run with: `python3 solution.py`

## 8. Test Cases

Test file: [`test_cases.py`](./test_cases.py) — 8 tests, all passing.

| ID | Input | Expected | Result |
|----|-------|----------|--------|
| TC-01 | 100 units | 500 | 500.0 — PASS |
| TC-02 | 150 units | 500 + 50*7 = 850 | 850.0 — PASS |
| TC-03 | 300 units | 500 + 1400 = 1900 | 1900.0 — PASS |
| TC-04 | 340 units | 1900 + 40*9 = 2260 | 2260.0 — PASS |
| TC-05 | First month 150 units | no rebate, total 917 | 917.0 — PASS |
| TC-06 | 260 after 280 | 5% rebate applied | rebate = 81.0 — PASS |
| TC-07 | 220 after 150 | no rebate | 0.0 — PASS |
| TC-08 | 150 -> 220 | increase 46.7% > 30% | flagged unusual — PASS |

## 9. Output

![Output screenshot](output_screenshot.png)

Full output: [`output.txt`](./output.txt)

```
Month    Units    Energy   Fixed    Cess   Rebate  Total(Rs)
Jun        150    850.00   50.00   17.00     0.00     917.00
Jul        220   1340.00   50.00   26.80     0.00    1416.80
Aug        340   2260.00   50.00   45.20     0.00    2355.20
Sep        280   1760.00   50.00   35.20    88.00    1757.20
Oct        260   1620.00   50.00   32.40    81.00    1621.40

MONTH-ON-MONTH COMPARISON:
  Jun -> Jul :  +46.7%  << UNUSUAL INCREASE (>30%)
  Jul -> Aug :  +54.5%  << UNUSUAL INCREASE (>30%)
```

## 10. Conclusion

The progressive billing program works correctly for slab calculation, cess, rebate and unusual-increase detection. I used a loop over slab tuples which made the code easy to change if rates change. The sample data shows two unusual increases (Jun to Jul and Jul to Aug) and rebates in Sep and Oct when consumption fell. All 8 test cases passed.
