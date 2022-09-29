"""
cd me

python.exe -m tests.test_fib
"""

from kernel.math.fib import make_fib

print("Test fib!")


def set_new_item(new_item):
    print(f"new: {new_item}")


fib = make_fib(end_num=128, set_new_item=set_new_item)
