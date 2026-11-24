"""
Case Study 05: Advanced Numeric Pattern Generator
Name: Akash, Roll No: 26000499
Syllabus used: nested loops, conditionals, strings, operators, validation
"""


def valid_size(n):
    """Size must be between 3 and 15."""
    if n < 3:
        return False
    if n > 15:
        return False
    return True


def hollow_diamond(n):
    """Return list of strings forming a hollow diamond of size n."""
    lines = []
    # top half including middle row
    for i in range(n):
        spaces = n - i - 1
        stars = 2 * i + 1
        line = " " * spaces
        if i == 0:
            line = line + "*"
        elif i == n - 1:
            line = line + "*" * stars
        else:
            line = line + "*" + " " * (stars - 2) + "*"
        lines.append(line)
    # bottom half
    for i in range(n - 2, -1, -1):
        spaces = n - i - 1
        stars = 2 * i + 1
        line = " " * spaces
        if i == 0:
            line = line + "*"
        else:
            line = line + "*" + " " * (stars - 2) + "*"
        lines.append(line)
    return lines


def number_pyramid(n):
    """Return list of strings: 1, 1 2 1, 1 2 3 2 1 ..."""
    lines = []
    for i in range(1, n + 1):
        nums = []
        for j in range(1, i + 1):
            nums.append(str(j))
        for j in range(i - 1, 0, -1):
            nums.append(str(j))
        line = " ".join(nums)
        lines.append(line)
    return lines


def main():
    n = 7
    print("=" * 50)
    print("  NUMERIC PATTERN GENERATOR")
    print("=" * 50)
    print("Size n = %d" % n)
    print("Valid size range: 3 to 15")
    print("-" * 50)

    if not valid_size(n):
        print("Invalid size! Please enter a value between 3 and 15.")
    else:
        print("\nHollow diamond (size %d):" % n)
        for line in hollow_diamond(n):
            print(line)

        print("\nNumeric pyramid (size %d):" % n)
        # centre the pyramid roughly
        for line in number_pyramid(n):
            print(" " * (n - len(line) // 2 - 1) + line)

    print("-" * 50)
    print("Validation demo:")
    print("  n=2  -> valid? %s" % valid_size(2))
    print("  n=7  -> valid? %s" % valid_size(7))
    print("  n=20 -> valid? %s" % valid_size(20))


if __name__ == "__main__":
    main()
