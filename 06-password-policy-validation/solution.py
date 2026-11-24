"""
Case Study 06: Password Policy Validation Engine
Name: Akash, Roll No: 26000499
Syllabus used: strings, string methods, loops, if-else, operators
"""

MIN_LENGTH = 8
PROHIBITED = ["password", "123456", "admin", "qwerty"]
SPECIALS = "!@#$%^&*()-_=+[]{};:,.<>?"

SAMPLES = [
    "welcome",
    "Passw0rd",
    "Strong#Pass1",
    "aaabbbCCC123!",
    "admin@12345",
    "MyCampus#2026",
    "AAAAAAAAaaaa1111!",
]


def has_repeat_run(pw):
    """True if same character repeats 3 or more times in a row."""
    run = 1
    for i in range(1, len(pw)):
        if pw[i] == pw[i - 1]:
            run = run + 1
            if run >= 3:
                return True
        else:
            run = 1
    return False


def validate(pw):
    """Return list of problems. Empty list means password is valid."""
    errors = []

    if len(pw) < MIN_LENGTH:
        errors.append("length %d is below minimum %d" % (len(pw), MIN_LENGTH))

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    for ch in pw:
        if "A" <= ch <= "Z":
            has_upper = True
        elif "a" <= ch <= "z":
            has_lower = True
        elif "0" <= ch <= "9":
            has_digit = True
        elif ch in SPECIALS:
            has_special = True

    if not has_upper:
        errors.append("missing an uppercase letter (A-Z)")
    if not has_lower:
        errors.append("missing a lowercase letter (a-z)")
    if not has_digit:
        errors.append("missing a digit (0-9)")
    if not has_special:
        errors.append("missing a special character like ! @ # $")

    lower = pw.lower()
    for word in PROHIBITED:
        if word in lower:
            errors.append("contains prohibited word '%s'" % word)

    if has_repeat_run(pw):
        errors.append("has 3 or more same characters in a row")

    return errors


def main():
    print("=" * 70)
    print("  PASSWORD POLICY VALIDATION ENGINE")
    print("=" * 70)
    print("Policy: length >= %d, need upper + lower + digit + special," % MIN_LENGTH)
    print("no prohibited words %s, no 3-in-a-row repeats." % PROHIBITED)
    print("-" * 70)

    passed = 0
    for pw in SAMPLES:
        errors = validate(pw)
        if len(errors) == 0:
            passed = passed + 1
            print("  [ PASS ] %-20s -> accepted" % pw)
        else:
            print("  [ FAIL ] %-20s -> %d problem(s)" % (pw, len(errors)))
            for e in errors:
                print("            * %s" % e)

    print("-" * 70)
    print("Result: %d of %d sample passwords satisfy the policy." % (passed, len(SAMPLES)))


if __name__ == "__main__":
    main()
