"""
cd me

python.exe -m tests.test_grundy
"""

from kernel.math.grundy import GrundySequence

print("Test grundy!")

len_N = 31
"""N は 山の石の数。このゲームでの最大数"""

S = {1, 2, 3}
"""S は サブトラクションセット"""

grundy_sequence = GrundySequence.make(S=S, len_N=len_N)

for i in range(0, len_N+1):
    grundy = grundy_sequence.get_grundy_at(i)
    print(f"i:{i} grundy:{grundy}")
