"""Test cases for Case Study 01 - University Scholarship Allocation."""
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

# S101 should be eligible
ok, agg, reasons = sol.check_eligibility(sol.APPLICANTS[0])
check("S101 eligible, aggregate 80.8", ok and abs(agg - 80.8) < 0.01 and reasons == [])

# S102 aggregate too low
ok, agg, reasons = sol.check_eligibility(sol.APPLICANTS[1])
check("S102 rejected, aggregate 58.6", (not ok) and abs(agg - 58.6) < 0.01)

# subject-wise check
ok, _, reasons = sol.check_eligibility(sol.APPLICANTS[1])
check("S102 Physics below 50 reported", any("Physics" in r for r in reasons))

# income check
ok, _, reasons = sol.check_eligibility(sol.APPLICANTS[2])
check("S103 income above limit reported", (not ok) and any("income" in r for r in reasons))

# attendance check
ok, _, reasons = sol.check_eligibility(sol.APPLICANTS[5])
check("S106 attendance below 75 reported", (not ok) and any("attendance" in r for r in reasons))

# ranking: Fatima first
eligible = []
for a in sol.APPLICANTS:
    ok, agg, _ = sol.check_eligibility(a)
    if ok:
        eligible.append((a[0], a[1], round(agg, 2), a[3], a[4]))
eligible.sort(key=sol.rank_key)
check("S105 ranked first", eligible[0][0] == "S105")

# tie break: S108 (88%) above S104 (76%) at same 61.4
pos = {}
for i in range(len(eligible)):
    pos[eligible[i][0]] = i
check("tie S108 above S104 by attendance", eligible[pos["S108"]][2] == eligible[pos["S104"]][2] and pos["S108"] < pos["S104"])

# counts
ok_count = 0
for a in sol.APPLICANTS:
    if sol.check_eligibility(a)[0]:
        ok_count += 1
check("4 eligible and 4 rejected", ok_count == 4 and len(sol.APPLICANTS) - ok_count == 4)

print("\nALL %d TESTS PASSED (Case Study 01)" % passed)
