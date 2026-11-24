"""Test cases for Case Study 10 - Smart Campus Management Simulation."""
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

# reset state
sol.students.clear()
sol.attendance.clear()
sol.marks.clear()
sol.registrations.clear()
for res in sol.resources:
    res[2] = 0

ok, msg = sol.add_student("S101", "Ananya")
check("add student works", ok == True)
ok, msg = sol.add_student("S101", "Duplicate")
check("duplicate roll rejected", ok == False)

ok, msg = sol.record_attendance("S101", 40, 50)
check("attendance recorded", ok == True)
ok, msg = sol.record_attendance("S999", 10, 20)
check("unknown student attendance rejected", ok == False)
ok, msg = sol.record_attendance("S101", 60, 50)
check("present > total rejected", ok == False)

ok, msg = sol.enter_marks("S101", 80, 75, 90)
check("marks entered", ok == True)
ok, msg = sol.enter_marks("S101", 110, 75, 90)
check("marks > 100 rejected", ok == False)

ok, msg = sol.register_event("S101", "Hackathon")
check("event registration works", ok == True)
ok, msg = sol.register_event("S101", "Hackathon")
check("duplicate registration rejected", ok == False)

ok, msg = sol.allocate_resource("Projector", 2)
check("resource allocation works", ok == True)
ok, msg = sol.allocate_resource("Projector", 10)
check("over-allocation rejected", ok == False)
ok, msg = sol.allocate_resource("Unknown", 1)
check("unknown resource rejected", ok == False)

print("\nALL %d TESTS PASSED (Case Study 10)" % passed)
