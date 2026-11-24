"""Test cases for Case Study 04 - Nested Loop Examination Seating Generator."""
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

check("reserved (1,2) detected", sol.is_reserved(1, 2) == True)
check("normal seat (1,1) not reserved", sol.is_reserved(1, 1) == False)
check("reserved (4,6) detected", sol.is_reserved(4, 6) == True)

grid = sol.generate()
check("grid has 4 rows", len(grid) == 4)
check("each row has 6 columns", len(grid[0]) == 6 and len(grid[3]) == 6)
check("RES at row1 col2", grid[0][1] == "RES")
check("first roll is 101", grid[0][0] == "101")

# count RES cells
count = 0
for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] == "RES":
            count += 1
check("5 reserved cells in grid", count == 5)

# rolls are unique
rolls = []
for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] != "RES":
            rolls.append(grid[r][c])
check("19 unique rolls", len(rolls) == 19 and len(set(rolls)) == 19)

print("\nALL %d TESTS PASSED (Case Study 04)" % passed)
