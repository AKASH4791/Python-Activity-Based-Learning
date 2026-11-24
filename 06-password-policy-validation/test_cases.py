"""Test cases for Case Study 06 - Password Policy Validation Engine."""
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

check("Strong#Pass1 is valid", sol.validate("Strong#Pass1") == [])
check("MyCampus#2026 is valid", sol.validate("MyCampus#2026") == [])
check("welcome fails length", len(sol.validate("welcome")) > 0)
check("Passw0rd fails (prohibited + no special)", len(sol.validate("Passw0rd")) > 0)
check("aaabbbCCC123! fails repeat run", any("3 or more" in e for e in sol.validate("aaabbbCCC123!")))
check("admin@12345 fails prohibited", any("prohibited" in e for e in sol.validate("admin@12345")))
check("AAAAAAAAaaaa1111! fails repeat", any("3 or more" in e for e in sol.validate("AAAAAAAAaaaa1111!")))
check("has_repeat_run detects aaa", sol.has_repeat_run("xxaaayy") == True)
check("has_repeat_run ok for abc", sol.has_repeat_run("abc123") == False)

print("\nALL %d TESTS PASSED (Case Study 06)" % passed)
