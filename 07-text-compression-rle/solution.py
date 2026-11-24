"""
Case Study 07: Text Compression Using Character Runs
Name: Akash, Roll No: 26000499
Syllabus used: strings, loops, conditionals, operators, lists
"""

SAMPLES = [
    "aaabbbcc",
    "abc",
    "aaaa",
    "mississippi",
    "aabbaabb",
    "hello",
    "aaabaaa",
]


def compress(s):
    """Run-length encode: aaabbb -> a3b3. Single chars stay as-is if count 1."""
    if len(s) == 0:
        return ""
    result = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count = count + 1
        else:
            if count == 1:
                result = result + s[i - 1]
            else:
                result = result + s[i - 1] + str(count)
            count = 1
    # last run
    if count == 1:
        result = result + s[len(s) - 1]
    else:
        result = result + s[len(s) - 1] + str(count)
    return result


def decompress(s):
    """Decode a run-length string back to original."""
    result = ""
    i = 0
    while i < len(s):
        ch = s[i]
        i = i + 1
        num = ""
        while i < len(s) and "0" <= s[i] <= "9":
            num = num + s[i]
            i = i + 1
        if num == "":
            result = result + ch
        else:
            n = int(num)
            for k in range(n):
                result = result + ch
    return result


def main():
    print("=" * 70)
    print("  TEXT COMPRESSION USING CHARACTER RUNS (RLE)")
    print("=" * 70)
    print("%-14s %-14s %8s %8s  %s" % ("Original", "Encoded", "Orig len", "Enc len", "Useful?"))
    print("-" * 70)
    for s in SAMPLES:
        enc = compress(s)
        useful = "yes" if len(enc) < len(s) else "no"
        print("%-14s %-14s %8d %8d  %s" % (s, enc, len(s), len(enc), useful))

    print("-" * 70)
    print("\nDecode check (encoded -> original):")
    for s in SAMPLES:
        enc = compress(s)
        dec = decompress(enc)
        ok = "OK" if dec == s else "MISMATCH"
        print("  %-14s -> %-14s -> %-14s [%s]" % (s, enc, dec, ok))

    print("\nNote: encoding is useful only when there are repeated characters.")
    print("For strings like 'abc' the encoded form is longer, so we keep original.")


if __name__ == "__main__":
    main()
