"""
cd me/docs/idea_sketch/s_4_5_40

python.exe make_pred_list.py

Explanation
===========
適当な S={ a, b, c } を選び、周期の予想を３つ出す いい加減なプログラム
"""
from make_c_from_a_b import get_3_periods_given_a_b_c

if __name__ == "__main__":
    for a in range(1, 10):
        for b in range(a+1, a+1+10):
            for z in range(1, 11):  # ab の定数倍
                c = a * b * z

                a_p_b, b_p_c, a_p_c = get_3_periods_given_a_b_c(a, b, c)
                """S = { a, b, c } を渡すと、周期の候補を３つ返す"""

                print(
                    f"S = {{ {a:2}, {b:2}, {c:3} }}  Period: Maybe    {a_p_b}    {b_p_c}    {a_p_c}")
