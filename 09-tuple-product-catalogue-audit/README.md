# Tuple-Based Product Catalogue Audit

Name: Akash  
Roll No: 26000499

## Problem statement

Store product identifiers, prices, and stock quantities in tuples; detect invalid records, calculate inventory values, and identify items requiring replenishment.

Each product is a tuple `(code, name, price, stock, reorder level)`. Invalid means empty code/name, price <= 0, stock < 0, or reorder < 0. Inventory value is price × stock. Replenishment is needed when stock <= reorder level.

## Objectives

- Store catalogue as a list of tuples.
- Use tuple unpacking to read each record.
- Validate records with conditionals and collect problems.
- Calculate inventory value with operators and loops.
- Identify replenishment items.

## Assumptions

- Price and stock are integers (price in rupees).
- Reorder level is the minimum stock before ordering more.
- Invalid records are excluded from inventory value calculation.
- 8 sample products are used, including 2 invalid ones for testing.

## Algorithm

```
1. START
2. FOR each product tuple in PRODUCTS:
   2.1 Unpack into code, name, price, stock, reorder
   2.2 problems = []
   2.3 IF code = "" THEN add "empty code"
   2.4 IF name = "" THEN add "empty name"
   2.5 IF price <= 0 THEN add "price must be positive"
   2.6 IF stock < 0 THEN add "stock cannot be negative"
   2.7 IF problems empty THEN valid list ELSE invalid list
3. Print valid table and invalid records with reasons
4. total_value = 0
   FOR each valid product: value = price * stock, total_value += value
5. FOR each valid product: IF stock <= reorder THEN print "order more"
6. Print summary counts
7. END
```

## Flowchart

![Flowchart](flowchart.png)

## Pseudocode

```
BEGIN CATALOGUE_AUDIT
    PRODUCTS <- [(code, name, price, stock, reorder), ...]
    valid <- [], invalid <- []

    FOR each p IN PRODUCTS DO
        (code, name, price, stock, reorder) <- p
        problems <- []
        IF code = "" THEN APPEND "empty code" TO problems
        IF name = "" THEN APPEND "empty name" TO problems
        IF price <= 0 THEN APPEND "price must be positive" TO problems
        IF stock < 0 THEN APPEND "stock negative" TO problems
        IF LENGTH(problems) = 0 THEN APPEND p TO valid
        ELSE APPEND (p, problems) TO invalid
    END FOR

    total <- 0
    FOR each (code, name, price, stock, reorder) IN valid DO
        total <- total + price * stock
    END FOR

    FOR each valid product DO
        IF stock <= reorder THEN PRINT "needs replenishment"
    END FOR
    PRINT summary
END
```

## Python source code

```python
"""
Case Study 09: Tuple-Based Product Catalogue Audit
Name: Akash, Roll No: 26000499
Syllabus used: tuples, tuple unpacking, loops, conditionals, operators, lists
"""

# each product is a tuple: (code, name, price, stock, reorder level)
PRODUCTS = [
    ("P101", "Notebook", 60, 120, 20),
    ("P102", "Pen", 15, 8, 50),
    ("P103", "Pencil Box", 120, 45, 15),
    ("P104", "Eraser", 10, 200, 30),
    ("P105", "Scale", 35, 0, 10),
    ("P106", "Marker", 45, 25, 25),
    ("", "Unknown Item", 50, 10, 5),
    ("P108", "Bad Price Item", -20, 10, 5),
]


def check_product(p):
    """Return list of problems for one product tuple. Empty = valid."""
    code, name, price, stock, reorder = p  # tuple unpacking
    problems = []
    if code == "":
        problems.append("empty product code")
    if name == "":
        problems.append("empty product name")
    if price <= 0:
        problems.append("price must be positive, got %d" % price)
    if stock < 0:
        problems.append("stock cannot be negative, got %d" % stock)
    if reorder < 0:
        problems.append("reorder level cannot be negative")
    return problems


def main():
    print("=" * 78)
    print("  PRODUCT CATALOGUE AUDIT")
    print("=" * 78)
    print("%-8s %-18s %8s %8s %8s" % ("Code", "Name", "Price", "Stock", "Reorder"))
    print("-" * 78)

    valid = []
    invalid = []
    for p in PRODUCTS:
        code, name, price, stock, reorder = p
        problems = check_product(p)
        if len(problems) == 0:
            valid.append(p)
            print("%-8s %-18s %8d %8d %8d" % (code, name, price, stock, reorder))
        else:
            invalid.append((p, problems))
            print("%-8s %-18s %8d %8d %8d  [INVALID]" % (code, name, price, stock, reorder))

    print("-" * 78)
    print("\nINVALID RECORDS:")
    if len(invalid) == 0:
        print("  None")
    for p, problems in invalid:
        code, name, price, stock, reorder = p
        print("  %s (%s):" % (code, name))
        for prob in problems:
            print("     - %s" % prob)

    print("\nINVENTORY VALUE (valid items only):")
    total_value = 0
    for code, name, price, stock, reorder in valid:
        value = price * stock
        total_value = total_value + value
        print("  %-8s %-18s Rs %d x %d = Rs %d" % (code, name, price, stock, value))
    print("  Total inventory value: Rs %d" % total_value)

    print("\nREPLENISHMENT NEEDED (stock <= reorder level):")
    need = 0
    for code, name, price, stock, reorder in valid:
        if stock <= reorder:
            need = need + 1
            print("  %-8s %-18s stock %d <= reorder %d -> order more" % (code, name, stock, reorder))
    if need == 0:
        print("  None")

    print("\nSummary: %d valid, %d invalid, %d need replenishment." % (len(valid), len(invalid), need))


if __name__ == "__main__":
    main()
```

## Test cases

```python
"""Test cases for Case Study 09 - Tuple-Based Product Catalogue Audit."""
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

check("P101 valid", sol.check_product(sol.PRODUCTS[0]) == [])
check("P102 valid (low stock is not invalid)", sol.check_product(sol.PRODUCTS[1]) == [])
check("empty code invalid", len(sol.check_product(sol.PRODUCTS[6])) > 0)
check("negative price invalid", any("price" in p for p in sol.check_product(sol.PRODUCTS[7])))
check("negative stock invalid", len(sol.check_product(("P1", "X", 10, -5, 5))) > 0)
check("empty name invalid", len(sol.check_product(("P1", "", 10, 5, 5))) > 0)

# inventory value of valid items
valid = []
for p in sol.PRODUCTS:
    if len(sol.check_product(p)) == 0:
        valid.append(p)
check("6 valid products", len(valid) == 6)

total = 0
for code, name, price, stock, reorder in valid:
    total = total + price * stock
# 60*120=7200, 15*8=120, 120*45=5400, 10*200=2000, 35*0=0, 45*25=1125 => 15845
check("total value 15845", total == 15845)

# replenishment: P102 (8<=50), P105 (0<=10), P106 (25<=25) => 3
need = 0
for code, name, price, stock, reorder in valid:
    if stock <= reorder:
        need = need + 1
check("3 items need replenishment", need == 3)

print("\nALL %d TESTS PASSED (Case Study 09)" % passed)
```

## Output screenshot

```
==============================================================================
  PRODUCT CATALOGUE AUDIT
==============================================================================
Code     Name                  Price    Stock  Reorder
------------------------------------------------------------------------------
P101     Notebook                 60      120       20
P102     Pen                      15        8       50
P103     Pencil Box              120       45       15
P104     Eraser                   10      200       30
P105     Scale                    35        0       10
P106     Marker                   45       25       25
         Unknown Item             50       10        5  [INVALID]
P108     Bad Price Item          -20       10        5  [INVALID]
------------------------------------------------------------------------------

INVALID RECORDS:
   (Unknown Item):
     - empty product code
  P108 (Bad Price Item):
     - price must be positive, got -20

INVENTORY VALUE (valid items only):
  P101     Notebook           Rs 60 x 120 = Rs 7200
  P102     Pen                Rs 15 x 8 = Rs 120
  P103     Pencil Box         Rs 120 x 45 = Rs 5400
  P104     Eraser             Rs 10 x 200 = Rs 2000
  P105     Scale              Rs 35 x 0 = Rs 0
  P106     Marker             Rs 45 x 25 = Rs 1125
  Total inventory value: Rs 15845

REPLENISHMENT NEEDED (stock <= reorder level):
  P102     Pen                stock 8 <= reorder 50 -> order more
  P105     Scale              stock 0 <= reorder 10 -> order more
  P106     Marker             stock 25 <= reorder 25 -> order more

Summary: 6 valid, 2 invalid, 3 need replenishment.
```

![Output screenshot](output_screenshot.png)

## Conclusion

Tuples worked well for storing fixed-format product records, and unpacking made the code readable. Out of 8 products, 6 were valid and 2 were invalid. Total inventory value of valid items is Rs 15,845, and 3 items need replenishment. All 9 test cases passed.
