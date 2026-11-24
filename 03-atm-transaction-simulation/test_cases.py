"""Test cases for Case Study 03 - ATM Transaction Sequence Simulation."""
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

b, s, m = sol.process(10000, ("deposit", 5000))
check("deposit works", b == 15000 and s == "OK")

b, s, m = sol.process(15000, ("withdraw", 3000))
check("withdraw works", b == 12000 and s == "OK")

b, s, m = sol.process(12000, ("withdraw", 25000))
check("over-limit withdraw rejected", b == 12000 and s == "REJECTED")

b, s, m = sol.process(5000, ("withdraw", 8000))
check("insufficient balance rejected", b == 5000 and s == "REJECTED")

b, s, m = sol.process(5000, ("deposit", -1000))
check("negative amount rejected", b == 5000 and s == "REJECTED")

b, s, m = sol.process(5000, ("deposit", 0))
check("zero amount rejected", b == 5000 and s == "REJECTED")

# full sequence closing balance
bal = sol.OPENING_BALANCE
for txn in sol.TRANSACTIONS:
    bal, _, _ = sol.process(bal, txn)
check("closing balance is 12000", bal == 12000)

print("\nALL %d TESTS PASSED (Case Study 03)" % passed)
