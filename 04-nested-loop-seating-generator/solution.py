"""
Case Study 04: Nested Loop Examination Seating Generator
Name: Akash, Roll No: 26000499
Syllabus used: nested loops, lists, tuples, conditionals, operators
"""

ROWS = 4
COLS = 6
# reserved seats as (row, col) tuples, 1-based
RESERVED = [(1, 2), (2, 5), (3, 3), (4, 1), (4, 6)]
START_ROLL = 101


def is_reserved(r, c):
    """Check if seat (r, c) is reserved. r and c are 1-based."""
    for rr, cc in RESERVED:  # tuple unpacking
        if rr == r and cc == c:
            return True
    return False


def generate():
    """Build the seating grid as a list of lists."""
    grid = []
    roll = START_ROLL
    for r in range(1, ROWS + 1):
        row = []
        for c in range(1, COLS + 1):
            if is_reserved(r, c):
                row.append("RES")
            else:
                row.append(str(roll))
                roll = roll + 1
        grid.append(row)
    return grid


def main():
    total_seats = ROWS * COLS
    reserved_count = len(RESERVED)
    available = total_seats - reserved_count

    print("=" * 60)
    print("  EXAMINATION SEATING ARRANGEMENT")
    print("=" * 60)
    print("Rows: %d, Columns: %d, Total seats: %d" % (ROWS, COLS, total_seats))
    print("Reserved seats: %d, Available seats: %d" % (reserved_count, available))
    print("-" * 60)

    grid = generate()
    # header
    header = "     "
    for c in range(1, COLS + 1):
        header = header + "%6d" % c
    print(header)
    print("-" * 60)
    for r in range(len(grid)):
        line = "R%-3d" % (r + 1)
        for c in range(len(grid[r])):
            line = line + "%6s" % grid[r][c]
        print(line)
    print("-" * 60)

    print("\nReserved seat positions (row, col):")
    for rr, cc in RESERVED:
        print("  Row %d, Column %d" % (rr, cc))

    print("\nCapacity check:")
    if available >= 20:
        print("  OK: %d available seats are enough for 20 students." % available)
    else:
        print("  WARNING: only %d seats available, not enough for 20 students." % available)

    # alternate seating note: even rows start from column 2 in some halls
    print("\nNote: seats marked RES are kept empty for invigilator / late students.")


if __name__ == "__main__":
    main()
