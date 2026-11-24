"""Test cases for Case Study 08 - Student Marks Matrix Analysis."""
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

check("grade A for 90", sol.grade_of(90) == "A (Distinction)")
check("grade B for 75", sol.grade_of(75) == "B (First Class)")
check("grade C for 60", sol.grade_of(60) == "C (Second Class)")
check("grade D for 40", sol.grade_of(40) == "D (Third Class)")

# Fatima total = 91+88+94+87+96 = 456
total = 0
for m in sol.MARKS[4]:
    total = total + m
check("Fatima total 456", total == 456)

# Maths column average = (82+55+74+61+91)/5 = 72.6
total = 0
for r in range(5):
    total = total + sol.MARKS[r][0]
avg = total / 5
check("Maths average 72.6", abs(avg - 72.6) < 0.01)

# highest mark is 96
high = -1
for r in range(5):
    for c in range(5):
        if sol.MARKS[r][c] > high:
            high = sol.MARKS[r][c]
check("highest mark 96", high == 96)

# lowest mark is 48
low = 101
for r in range(5):
    for c in range(5):
        if sol.MARKS[r][c] < low:
            low = sol.MARKS[r][c]
check("lowest mark 48", low == 48)

print("\nALL %d TESTS PASSED (Case Study 08)" % passed)
