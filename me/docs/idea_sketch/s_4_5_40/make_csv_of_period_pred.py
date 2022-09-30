"""
cd me/docs/idea_sketch/s_4_5_40

python.exe make_csv_of_period_pred.py

Explanation
===========
適当な S={ a, b, c } を選び、周期の予想を３つ出す いい加減なプログラム
"""
from make_c_from_a_b import get_3_periods_given_a_b_c

if __name__ == "__main__":

    text = ""
    text += "a,b,c,p1,p2,p3,correct\n"
    """S = { a, b, c } Period predict: p1, p2, p3 and Correct period"""

    for a in range(1, 10):
        for b in range(a+1, a+1+10):
            for z in range(1, 11):  # ab の定数倍
                c = a * b * z

                a_p_b, b_p_c, a_p_c = get_3_periods_given_a_b_c(a, b, c)
                """S = { a, b, c } を渡すと、周期の候補を３つ返す"""

                text += f"{a},{b},{c},{a_p_b},{b_p_c},{a_p_c},-1\n"

    with open('./period_pred_tmp.csv', 'w', encoding="utf-8") as f:
        f.write(text)
