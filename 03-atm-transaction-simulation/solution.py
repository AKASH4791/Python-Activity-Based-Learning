"""
Case Study 03: ATM Transaction Sequence Simulation
Name: Akash, Roll No: 26000499
Syllabus used: variables, operators, if-else, loops, lists, tuples, unpacking
"""

OPENING_BALANCE = 10000
MAX_WITHDRAW_PER_TXN = 20000

# each transaction is a tuple: (type, amount)
# type is "deposit" or "withdraw"
TRANSACTIONS = [
    ("deposit", 5000),
    ("withdraw", 3000),
    ("withdraw", 25000),
    ("withdraw", 20000),
    ("deposit", -1000),
    ("withdraw", 1500),
    ("deposit", 2000),
    ("withdraw", 500),
]


def process(balance, txn):
    """Process one transaction.
    Returns (new_balance, status, message)."""
    ttype, amount = txn  # tuple unpacking
    if amount <= 0:
        return balance, "REJECTED", "amount must be positive"
    if ttype == "deposit":
        return balance + amount, "OK", "deposited Rs %d" % amount
    elif ttype == "withdraw":
        if amount > MAX_WITHDRAW_PER_TXN:
            return balance, "REJECTED", "exceeds per-transaction limit Rs %d" % MAX_WITHDRAW_PER_TXN
        if amount > balance:
            return balance, "REJECTED", "insufficient balance"
        return balance - amount, "OK", "withdrew Rs %d" % amount
    else:
        return balance, "REJECTED", "unknown transaction type"


def main():
    balance = OPENING_BALANCE
    print("=" * 70)
    print("  ATM TRANSACTION SEQUENCE SIMULATION")
    print("=" * 70)
    print("Opening balance : Rs %d" % balance)
    print("Per-transaction withdrawal limit : Rs %d" % MAX_WITHDRAW_PER_TXN)
    print("-" * 70)
    print("%-4s %-10s %10s %-10s %10s" % ("#", "Type", "Amount", "Status", "Balance"))
    print("-" * 70)

    ok_count = 0
    rejected_count = 0
    total_deposit = 0
    total_withdraw = 0

    for i in range(len(TRANSACTIONS)):
        txn = TRANSACTIONS[i]
        ttype, amount = txn
        balance, status, msg = process(balance, txn)
        if status == "OK":
            ok_count = ok_count + 1
            if ttype == "deposit":
                total_deposit = total_deposit + amount
            else:
                total_withdraw = total_withdraw + amount
        else:
            rejected_count = rejected_count + 1
        print("%-4d %-10s %10d %-10s %10d" % (i + 1, ttype, amount, status, balance))
        if status == "REJECTED":
            print("      -> %s" % msg)

    print("-" * 70)
    print("SUMMARY:")
    print("  Successful transactions : %d" % ok_count)
    print("  Rejected transactions   : %d" % rejected_count)
    print("  Total deposited         : Rs %d" % total_deposit)
    print("  Total withdrawn         : Rs %d" % total_withdraw)
    print("  Closing balance         : Rs %d" % balance)


if __name__ == "__main__":
    main()
