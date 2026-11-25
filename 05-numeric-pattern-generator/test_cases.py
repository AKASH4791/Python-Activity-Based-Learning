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
