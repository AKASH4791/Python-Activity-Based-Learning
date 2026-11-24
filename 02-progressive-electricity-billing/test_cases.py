"""Test cases for Case Study 02 - Progressive Electricity Billing."""
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

check("100 units = 500", abs(sol.slab_charge(100) - 500.0) < 0.01)
check("150 units = 500+350=850", abs(sol.slab_charge(150) - 850.0) < 0.01)
check("300 units = 500+1400=1900", abs(sol.slab_charge(300) - 1900.0) < 0.01)
check("340 units = 1900+360=2260", abs(sol.slab_charge(340) - 2260.0) < 0.01)

e, c, r, t = sol.compute_bill(150, None)
check("first month no rebate", r == 0.0 and abs(t - (850 + 50 + 17.0)) < 0.01)

e, c, r, t = sol.compute_bill(260, 280)
check("decrease gives 5% rebate", abs(r - round(e * 0.05, 2)) < 0.01)

e, c, r, t = sol.compute_bill(220, 150)
check("increase gives no rebate", r == 0.0)

# unusual increase detection: 150 -> 220 is 46.7% > 30%
change = (220 - 150) / 150
check("Jun->Jul is unusual increase", change > 0.30)

print("\nALL %d TESTS PASSED (Case Study 02)" % passed)
