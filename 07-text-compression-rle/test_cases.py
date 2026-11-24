"""Test cases for Case Study 07 - Text Compression Using Character Runs."""
import importlib.util
import os

spec = importlib.util.spec_from_file_location("sol", os.path.join(os.path.dirname(__file__), "solution.py"))
sol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol)

passed = 0

def check(label, condition):
    global passed
    assert condition, "FAILED: " + label
    passed += 1
    print("  PASS:", label)

check("aaabbbcc -> a3b3c2", sol.compress("aaabbbcc") == "a3b3c2")
check("abc stays abc", sol.compress("abc") == "abc")
check("aaaa -> a4", sol.compress("aaaa") == "a4")
check("empty stays empty", sol.compress("") == "")
check("single char", sol.compress("x") == "x")
check("mississippi roundtrip", sol.decompress(sol.compress("mississippi")) == "mississippi")
check("aaabaaa roundtrip", sol.decompress(sol.compress("aaabaaa")) == "aaabaaa")
check("aabbaabb -> a2b2a2b2", sol.compress("aabbaabb") == "a2b2a2b2")
check("hello -> hel2o", sol.compress("hello") == "hel2o")

print("\nALL %d TESTS PASSED (Case Study 07)" % passed)
