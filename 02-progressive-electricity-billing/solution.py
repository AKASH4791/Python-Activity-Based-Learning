"""
Case Study 02: Progressive Electricity Billing
Name: Akash, Roll No: 26000499
Syllabus used: variables, operators, if-else, loops, lists, tuples, unpacking
"""

# slabs as tuples: (slab upper limit, rate per unit)
SLABS = [(100, 5.0), (300, 7.0), (500, 9.0), (1000000, 12.0)]
FIXED_CHARGE = 50.0
CESS_RATE = 0.02
REBATE_RATE = 0.05
UNUSUAL_LIMIT = 0.30

# (month, units consumed)
MONTHS = [
    ("Jun", 150),
    ("Jul", 220),
    ("Aug", 340),
    ("Sep", 280),
    ("Oct", 260),
]


def slab_charge(units):
    """Calculate energy charge slab by slab."""
    remaining = units
    lower = 0
    charge = 0.0
    for limit, rate in SLABS:  # tuple unpacking
        if remaining <= 0:
            break
        slab_units = remaining
        if slab_units > limit - lower:
            slab_units = limit - lower
        charge = charge + slab_units * rate
        remaining = remaining - slab_units
        lower = limit
    return charge


def compute_bill(units, prev_units):
    """Returns (energy, cess, rebate, total) for one month."""
    energy = slab_charge(units)
    cess = energy * CESS_RATE
    rebate = 0.0
    if prev_units is not None and units < prev_units:
        rebate = energy * REBATE_RATE
    total = energy + FIXED_CHARGE + cess - rebate
    return round(energy, 2), round(cess, 2), round(rebate, 2), round(total, 2)


def main():
    bills = []
    prev = None
    for month, units in MONTHS:
        energy, cess, rebate, total = compute_bill(units, prev)
        bills.append((month, units, energy, cess, rebate, total))
        prev = units

    print("=" * 82)
    print("  PROGRESSIVE ELECTRICITY BILL STATEMENT")
    print("=" * 82)
    print("%-6s %7s %9s %7s %7s %8s %10s" % ("Month", "Units", "Energy", "Fixed", "Cess", "Rebate", "Total(Rs)"))
    print("-" * 82)
    for month, units, energy, cess, rebate, total in bills:
        print("%-6s %7d %9.2f %7.2f %7.2f %8.2f %10.2f" % (month, units, energy, FIXED_CHARGE, cess, rebate, total))
    print("-" * 82)

    print("\nMONTH-ON-MONTH COMPARISON:")
    print("-" * 82)
    for i in range(1, len(bills)):
        m0, u0 = bills[i - 1][0], bills[i - 1][1]
        m1, u1 = bills[i][0], bills[i][1]
        change = (u1 - u0) / u0
        pct = change * 100
        flag = ""
        if change > UNUSUAL_LIMIT:
            flag = "  << UNUSUAL INCREASE (>30%)"
        elif change < 0:
            flag = "  (decrease, rebate applied)"
        print("  %s -> %s : %+6.1f%%%s" % (m0, m1, pct, flag))

    # highest and lowest bill
    hi_month = bills[0][0]
    hi_total = bills[0][5]
    lo_month = bills[0][0]
    lo_total = bills[0][5]
    for b in bills:
        if b[5] > hi_total:
            hi_total = b[5]
            hi_month = b[0]
        if b[5] < lo_total:
            lo_total = b[5]
            lo_month = b[0]
    print("\nHIGHEST BILL : %s (Rs %.2f)" % (hi_month, hi_total))
    print("LOWEST  BILL : %s (Rs %.2f)" % (lo_month, lo_total))


if __name__ == "__main__":
    main()
