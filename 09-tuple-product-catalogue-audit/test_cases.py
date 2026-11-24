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
