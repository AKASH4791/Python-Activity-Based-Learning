"""
Case Study 08: Student Marks Matrix Analysis
Name: Akash, Roll No: 26000499
Syllabus used: nested lists, loops, conditionals, operators
"""

SUBJECTS = ["Maths", "Physics", "Chemistry", "English", "CS"]
STUDENTS = ["Ananya", "Bharat", "Chitra", "Deepak", "Fatima"]

# rows = students, columns = subjects
MARKS = [
    [82, 76, 90, 71, 85],
    [55, 48, 62, 70, 58],
    [74, 69, 71, 66, 80],
    [61, 57, 64, 59, 66],
    [91, 88, 94, 87, 96],
]

WEAK_AVG = 70.0
RISK_AVG = 60.0


def grade_of(avg):
    if avg >= 85:
        return "A (Distinction)"
    if avg >= 70:
        return "B (First Class)"
    if avg >= 55:
        return "C (Second Class)"
    return "D (Third Class)"


def main():
    print("=" * 74)
    print("  STUDENT MARKS MATRIX ANALYSIS")
    print("=" * 74)
    header = "%-9s" % "Student"
    for s in SUBJECTS:
        header = header + "%10s" % s
    header = header + "%9s" % "Avg"
    print(header)
    print("-" * 74)
    for r in range(len(STUDENTS)):
        row = MARKS[r]
        total = 0
        for m in row:
            total = total + m
        avg = total / len(row)
        line = "%-9s" % STUDENTS[r]
        for m in row:
            line = line + "%10d" % m
        line = line + "%9.2f" % avg
        print(line)
    print("-" * 74)

    print("\nROW-WISE (per student):")
    best_total = -1
    best_index = -1
    for r in range(len(STUDENTS)):
        total = 0
        for m in MARKS[r]:
            total = total + m
        avg = total / len(MARKS[r])
        status = "AT RISK" if avg < RISK_AVG else "ok"
        print("  %-9s total=%3d  avg=%5.2f  grade=%-18s %s" % (STUDENTS[r], total, avg, grade_of(avg), status))
        if total > best_total:
            best_total = total
            best_index = r
    print("  -> Top performer: %s (%d marks)" % (STUDENTS[best_index], best_total))

    print("\nCOLUMN-WISE (per subject):")
    weak = []
    for c in range(len(SUBJECTS)):
        total = 0
        for r in range(len(STUDENTS)):
            total = total + MARKS[r][c]
        avg = total / len(STUDENTS)
        flag = ""
        if avg < WEAK_AVG:
            flag = "  << WEAK SUBJECT"
            weak.append(SUBJECTS[c])
        print("  %-10s average = %5.2f%s" % (SUBJECTS[c], avg, flag))

    high = -1
    low = 101
    hi_r = 0
    hi_c = 0
    lo_r = 0
    lo_c = 0
    for r in range(len(STUDENTS)):
        for c in range(len(SUBJECTS)):
            if MARKS[r][c] > high:
                high = MARKS[r][c]
                hi_r = r
                hi_c = c
            if MARKS[r][c] < low:
                low = MARKS[r][c]
                lo_r = r
                lo_c = c
    print("\nEXTRAMES:")
    print("  Highest: %d (%s in %s)" % (high, STUDENTS[hi_r], SUBJECTS[hi_c]))
    print("  Lowest : %d (%s in %s)" % (low, STUDENTS[lo_r], SUBJECTS[lo_c]))
    if len(weak) == 0:
        print("  Weak subjects (avg < %.0f): none" % WEAK_AVG)
    else:
        print("  Weak subjects (avg < %.0f): %s" % (WEAK_AVG, ", ".join(weak)))


if __name__ == "__main__":
    main()
