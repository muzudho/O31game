"""
cd me

python.exe -m tests.test_mex
"""

from kernel.math.mex import mex

print("Test mex!")

T = [0, 1, 2]
print(f"T:{T} mex:{mex(T)}")

T = [1, 2, 3]
print(f"T:{T} mex:{mex(T)}")

T = [0, 1, 3]
print(f"T:{T} mex:{mex(T)}")
