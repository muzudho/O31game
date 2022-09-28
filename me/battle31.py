# Author: Muzudho

import random

total = 31
numbers_to_choose = []


def main():
    global total, numbers_to_choose

    # Title
    print("""
＼ ──┐　┐　    ─┐   ┌─┐ ／
／ ──┤　│　┌─┐┌─┤├┬┐├─┘ ＼
＼ ──┘　┴　└─┤└─┴│││└─┘ ／
／          ─┘       .. ＼
＼ ..................   ／
／      ...........     ＼
""")

    # 取っていい石の数（複数）
    numerics = input("""
     ┌─┐
┌─┐┌─┼┬┴┐　？
└─┘└─┘└─┘
How many do you want to take at one time?
Example: s=1,2,3
s=""").split(",")
    numbers_to_choose = [int(numeric) for numeric in numerics]
    # 昇順ソート
    numbers_to_choose.sort()
    print(create_position_text(total, 0))

    while True:

        # 残りの石の数以上の選択肢は削除します
        while total < numbers_to_choose[len(numbers_to_choose)-1]:
            numbers_to_choose.pop(-1)

        # Your turn.

        while True:
            try:
                # 入力を並び替える
                numerics = [str(number) for number in numbers_to_choose]

                choose = " ".join(numerics)
                enter = input(f"""
 ┌──┐
   ┌┘
   ・
How many do you take?
Please choose: {choose}
> """)

                if enter == "quit" or enter == "exit":
                    print("Bye.")
                    exit(0)

                number_taken = int(enter)

                # 選択肢の中からちゃんと選んだら
                if number_taken in numbers_to_choose:
                    # ループから抜ける
                    break

                print("Please try again!")

            except Exception as e:
                print("Please try again!")
                # print(e)

        total -= number_taken
        print(create_position_text(total, number_taken))

        if total < 1:
            # 最後の石を取った
            print("You win!")
            break

        # 残りの石の数以上の選択肢は削除します
        while 0 < len(numbers_to_choose) and total < numbers_to_choose[len(numbers_to_choose)-1]:
            numbers_to_choose.pop(-1)

        # Opponent turn.
        number_taken = get_bestmove()
        print(f"""
  ┌─────┐
  │ ^ ^ │
  │  q  │
  └─┐ ┌─┘
┌───┘ └───┐
│         │ The computer took {number_taken} stone(s).""")
        total -= number_taken
        print(create_position_text(total, number_taken))

        if total < 1:
            # 最後の石を取られた
            print("You lose!")
            break

    # finished.


def create_position_text(rest, number_taken):
    s = """
"""

    for _ in range(0, rest):
        s += " "

    for _ in range(0, number_taken):
        s += "o"  # 取った石

    s += "\n"

    for _ in range(0, rest):
        s += "o"  # 残ってる石

    s += """
-------------------------------
         1111111111222222222233
1234567890123456789012345678901

"""

    return s


def get_bestmove():
    """コンピューターの選んだ数"""
    global total, numbers_to_choose

    win_count = [0] * len(numbers_to_choose)
    lose_count = [0] * len(numbers_to_choose)

    # TODO もっといろいろ思考したい
    playout_try_count = 50000  # プレイアウト回数。数字は適当
    for _ in range(0, playout_try_count):
        # 適当に選ぶ
        index = random.randint(0, len(numbers_to_choose)-1)
        choose = numbers_to_choose[index]

        numbers_to_choose_copy = numbers_to_choose[:]  # 配列はスライスを渡す
        isWin = playout(choose, total, numbers_to_choose_copy)
        if isWin:
            win_count[index] += 1
        else:
            lose_count[index] += 1

    # 勝率が一番高かった手を選ぶ
    high_rate = 0
    high_index = -1
    for index in range(0, len(numbers_to_choose)):
        total_num = win_count[index] + lose_count[index]
        if 0 < total_num:
            rate = win_count[index]/total_num

            # info
            print(
                f"[{numbers_to_choose[index]:2}] {rate:1.2f} = {win_count[index]}/{total_num}")

            if high_rate < rate:
                high_rate = rate
                high_index = index

    return numbers_to_choose[high_index]


def playout(choose, total_copy, numbers_to_choose_copy):
    # 再帰しなくてもいいや
    while True:
        # Computer turn
        total_copy -= choose
        if total_copy < 1:
            # コンピューターが全部の石を取ったら、コンピューターの勝ち
            return True

        # 残りの石の数以上の選択肢は削除します
        while total_copy < numbers_to_choose_copy[len(numbers_to_choose_copy)-1]:
            numbers_to_choose_copy.pop(-1)

            if len(numbers_to_choose_copy) < 1:
                # FIXME 相手に、選べる選択肢を残さなかったら、こっちの勝ち
                return True

        # Human turn
        # 適当に選ぶ
        num = random.choice(numbers_to_choose_copy)
        total_copy -= num

        if total_copy < 1:
            # 人間が全部の石を取ったら、コンピューターの負け
            return False

        # 残りの石の数以上の選択肢は削除します
        while total_copy < numbers_to_choose_copy[len(numbers_to_choose_copy)-1]:
            numbers_to_choose_copy.pop(-1)

            if len(numbers_to_choose_copy) < 1:
                # FIXME コンピューターに、選べる選択肢を残さなかったら、コンピューターの負け
                return False


def fewer_choices():
    """選択肢の減少"""
    pass


if __name__ == "__main__":
    main()
