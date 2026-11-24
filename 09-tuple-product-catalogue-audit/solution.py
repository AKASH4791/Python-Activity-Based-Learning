"""
Case Study 09: Tuple-Based Product Catalogue Audit
Name: Akash, Roll No: 26000499
Syllabus used: tuples, tuple unpacking, loops, conditionals, operators, lists
"""

# each product is a tuple: (code, name, price, stock, reorder level)
PRODUCTS = [
    ("P101", "Notebook", 60, 120, 20),
    ("P102", "Pen", 15, 8, 50),
    ("P103", "Pencil Box", 120, 45, 15),
    ("P104", "Eraser", 10, 200, 30),
    ("P105", "Scale", 35, 0, 10),
    ("P106", "Marker", 45, 25, 25),
    ("", "Unknown Item", 50, 10, 5),
    ("P108", "Bad Price Item", -20, 10, 5),
]


def check_product(p):
    """Return list of problems for one product tuple. Empty = valid."""
    code, name, price, stock, reorder = p  # tuple unpacking
    problems = []
    if code == "":
        problems.append("empty product code")
    if name == "":
        problems.append("empty product name")
    if price <= 0:
        problems.append("price must be positive, got %d" % price)
    if stock < 0:
        problems.append("stock cannot be negative, got %d" % stock)
    if reorder < 0:
        problems.append("reorder level cannot be negative")
    return problems


def main():
    print("=" * 78)
    print("  PRODUCT CATALOGUE AUDIT")
    print("=" * 78)
    print("%-8s %-18s %8s %8s %8s" % ("Code", "Name", "Price", "Stock", "Reorder"))
    print("-" * 78)

    valid = []
    invalid = []
    for p in PRODUCTS:
        code, name, price, stock, reorder = p
        problems = check_product(p)
        if len(problems) == 0:
            valid.append(p)
            print("%-8s %-18s %8d %8d %8d" % (code, name, price, stock, reorder))
        else:
            invalid.append((p, problems))
            print("%-8s %-18s %8d %8d %8d  [INVALID]" % (code, name, price, stock, reorder))

    print("-" * 78)
    print("\nINVALID RECORDS:")
    if len(invalid) == 0:
        print("  None")
    for p, problems in invalid:
        code, name, price, stock, reorder = p
        print("  %s (%s):" % (code, name))
        for prob in problems:
            print("     - %s" % prob)

    print("\nINVENTORY VALUE (valid items only):")
    total_value = 0
    for code, name, price, stock, reorder in valid:
        value = price * stock
        total_value = total_value + value
        print("  %-8s %-18s Rs %d x %d = Rs %d" % (code, name, price, stock, value))
    print("  Total inventory value: Rs %d" % total_value)

    print("\nREPLENISHMENT NEEDED (stock <= reorder level):")
    need = 0
    for code, name, price, stock, reorder in valid:
        if stock <= reorder:
            need = need + 1
            print("  %-8s %-18s stock %d <= reorder %d -> order more" % (code, name, stock, reorder))
    if need == 0:
        print("  None")

    print("\nSummary: %d valid, %d invalid, %d need replenishment." % (len(valid), len(invalid), need))


if __name__ == "__main__":
    main()
