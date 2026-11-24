"""
Case Study 01: University Scholarship Allocation
Name: Akash, Roll No: 26000499
Syllabus used: variables, data types, operators, if-else, loops,
lists, tuples, tuple unpacking, sorting
"""

MIN_AGGREGATE = 60.0
MIN_SUBJECT = 50
MIN_ATTENDANCE = 75.0
MAX_INCOME = 500000
SUBJECTS = ["Maths", "Physics", "Chemistry", "English", "CS"]

# each applicant is a tuple: (roll, name, marks list, attendance %, income)
APPLICANTS = [
    ("S101", "Ananya", [82, 76, 90, 71, 85], 92, 320000),
    ("S102", "Bharat", [55, 48, 62, 70, 58], 78, 480000),
    ("S103", "Chitra", [74, 69, 71, 66, 80], 84, 610000),
    ("S104", "Deepak", [61, 57, 64, 59, 66], 76, 495000),
    ("S105", "Fatima", [91, 88, 94, 87, 96], 97, 250000),
    ("S106", "Gopal", [58, 52, 49, 63, 55], 71, 300000),
    ("S107", "Harsha", [77, 72, 68, 74, 70], 80, 540000),
    ("S108", "Ishaan", [64, 58, 66, 60, 59], 88, 410000),
]


def check_eligibility(applicant):
    """Check one applicant. Returns (eligible, aggregate, reasons list)."""
    roll, name, marks, attendance, income = applicant  # tuple unpacking
    total = 0
    for m in marks:
        total = total + m
    aggregate = total / len(marks)
    reasons = []

    if aggregate < MIN_AGGREGATE:
        reasons.append("aggregate %.1f below %.0f" % (aggregate, MIN_AGGREGATE))

    for i in range(len(marks)):
        if marks[i] < MIN_SUBJECT:
            reasons.append("%s score %d below %d" % (SUBJECTS[i], marks[i], MIN_SUBJECT))

    if attendance < MIN_ATTENDANCE:
        reasons.append("attendance %.1f%% below %.0f%%" % (attendance, MIN_ATTENDANCE))

    if income > MAX_INCOME:
        reasons.append("family income %d above limit %d" % (income, MAX_INCOME))

    eligible = len(reasons) == 0
    return eligible, aggregate, reasons


def rank_key(record):
    """Sorting key: aggregate high to low, then attendance high to low,
    then income low to high, then roll number low to high."""
    roll, name, aggregate, attendance, income = record
    return (-aggregate, -attendance, income, roll)


def main():
    eligible = []
    rejected = []

    for applicant in APPLICANTS:
        ok, aggregate, reasons = check_eligibility(applicant)
        roll, name, marks, attendance, income = applicant
        if ok:
            eligible.append((roll, name, round(aggregate, 2), attendance, income))
        else:
            rejected.append((roll, name, reasons))

    eligible.sort(key=rank_key)

    print("=" * 74)
    print("  RANKED LIST OF ELIGIBLE SCHOLARSHIP APPLICANTS")
    print("=" * 74)
    print("%-5s %-9s %-10s %-11s %-10s" % ("Rank", "Roll", "Name", "Aggregate", "Attendance"))
    print("-" * 74)
    for i in range(len(eligible)):
        roll, name, aggregate, attendance, income = eligible[i]
        print("%-5d %-9s %-10s %-11.2f %-10s" % (i + 1, roll, name, aggregate, "%.1f%%" % attendance))
    print("-" * 74)

    print("\nTIE RESOLUTION LOG:")
    found_tie = False
    for i in range(len(eligible) - 1):
        if eligible[i][2] == eligible[i + 1][2]:
            found_tie = True
            a = eligible[i]
            b = eligible[i + 1]
            print("  Tie at aggregate %.2f between %s and %s -> broken by attendance (%.0f%% vs %.0f%%), higher attendance ranked first."
                  % (a[2], a[0], b[0], a[3], b[3]))
    if not found_tie:
        print("  No ties occurred.")

    print("\nREJECTED APPLICANTS:")
    print("-" * 74)
    for roll, name, reasons in rejected:
        print("  %s (%s):" % (roll, name))
        for r in reasons:
            print("     - %s" % r)
    print("-" * 74)
    print("Summary: %d eligible, %d rejected, %d total." % (len(eligible), len(rejected), len(APPLICANTS)))


if __name__ == "__main__":
    main()
