"""
Case Study 10: Comprehensive Smart Campus Management Simulation
Name: Akash, Roll No: 26000499
Syllabus used: menu loops, conditionals, strings, lists, nested lists,
tuples, tuple unpacking, operators
"""

# student record as tuple: (roll, name)
students = []
# attendance: list of [roll, present_days, total_days] -> nested list
attendance = []
# marks: list of [roll, [m1, m2, m3]]
marks = []
# event registrations: list of (roll, event_name)
registrations = []
# resources: list of [resource_name, available, allocated]
resources = [
    ["Projector", 5, 0],
    ["Laptop", 10, 0],
    ["Camera", 3, 0],
]
EVENT_FEE = 200


def find_student(roll):
    for r, n in students:
        if r == roll:
            return True
    return False


def add_student(roll, name):
    if find_student(roll):
        return False, "roll already exists"
    students.append((roll, name))
    return True, "added"


def record_attendance(roll, present, total):
    if not find_student(roll):
        return False, "student not found"
    if total <= 0 or present < 0 or present > total:
        return False, "invalid attendance values"
    for entry in attendance:
        if entry[0] == roll:
            entry[1] = present
            entry[2] = total
            return True, "updated"
    attendance.append([roll, present, total])
    return True, "recorded"


def enter_marks(roll, m1, m2, m3):
    if not find_student(roll):
        return False, "student not found"
    for m in [m1, m2, m3]:
        if m < 0 or m > 100:
            return False, "marks must be between 0 and 100"
    for entry in marks:
        if entry[0] == roll:
            entry[1] = [m1, m2, m3]
            return True, "updated"
    marks.append([roll, [m1, m2, m3]])
    return True, "entered"


def register_event(roll, event):
    if not find_student(roll):
        return False, "student not found"
    for r, e in registrations:
        if r == roll and e == event:
            return False, "already registered"
    registrations.append((roll, event))
    return True, "registered"


def allocate_resource(name, qty):
    if qty <= 0:
        return False, "quantity must be positive"
    for res in resources:
        if res[0] == name:
            if res[2] + qty > res[1]:
                return False, "not enough available"
            res[2] = res[2] + qty
            return True, "allocated"
    return False, "resource not found"


def summary():
    print("\n===== SUMMARY REPORT =====")
    print("Total students: %d" % len(students))
    print("\nStudents:")
    for roll, name in students:
        print("  %s - %s" % (roll, name))
    print("\nAttendance:")
    for roll, present, total in attendance:
        pct = (present / total) * 100
        print("  %s : %d/%d = %.1f%%" % (roll, present, total, pct))
    print("\nMarks (average):")
    for roll, mlist in marks:
        total = mlist[0] + mlist[1] + mlist[2]
        avg = total / 3
        print("  %s : %s avg %.2f" % (roll, mlist, avg))
    print("\nEvent registrations (fee Rs %d each):" % EVENT_FEE)
    for roll, event in registrations:
        print("  %s -> %s" % (roll, event))
    print("  Total fee collected: Rs %d" % (len(registrations) * EVENT_FEE))
    print("\nResources:")
    for name, avail, alloc in resources:
        print("  %s : allocated %d of %d" % (name, alloc, avail))


def main():
    print("=" * 60)
    print("  SMART CAMPUS MANAGEMENT SYSTEM")
    print("  Name: Akash, Roll No: 26000499")
    print("=" * 60)
    while True:
        print("\n--- MENU ---")
        print("1. Add student")
        print("2. Record attendance")
        print("3. Enter marks")
        print("4. Register for event")
        print("5. Allocate resource")
        print("6. Summary report")
        print("7. Exit")
        choice = input("Enter choice (1-7): ").strip()

        if choice == "1":
            roll = input("Roll number: ").strip()
            name = input("Student name: ").strip()
            ok, msg = add_student(roll, name)
            print("Result:", msg)
        elif choice == "2":
            roll = input("Roll number: ").strip()
            present = int(input("Present days: "))
            total = int(input("Total days: "))
            ok, msg = record_attendance(roll, present, total)
            print("Result:", msg)
        elif choice == "3":
            roll = input("Roll number: ").strip()
            m1 = int(input("Marks subject 1: "))
            m2 = int(input("Marks subject 2: "))
            m3 = int(input("Marks subject 3: "))
            ok, msg = enter_marks(roll, m1, m2, m3)
            print("Result:", msg)
        elif choice == "4":
            roll = input("Roll number: ").strip()
            event = input("Event name: ").strip()
            ok, msg = register_event(roll, event)
            print("Result:", msg)
        elif choice == "5":
            name = input("Resource name (Projector/Laptop/Camera): ").strip()
            qty = int(input("Quantity: "))
            ok, msg = allocate_resource(name, qty)
            print("Result:", msg)
        elif choice == "6":
            summary()
        elif choice == "7":
            print("Exiting. Thank you!")
            break
        else:
            print("Invalid choice. Please enter 1 to 7.")


if __name__ == "__main__":
    main()
