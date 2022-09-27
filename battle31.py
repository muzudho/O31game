import random

total = 31
numbers_to_choose = []


def main():
    global total, numbers_to_choose

    print("")
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

    while True:
        print(create_position_text(total))

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

                if enter == "quit":
                    print("Bye.")
                    exit(0)

                n = int(enter)
                if n in numbers_to_choose:
                    # ループから抜ける
                    break

            except Exception as e:
                print("Please try again!")
                # print(e)

        total -= n

        print(create_position_text(total))

        if total < 1:
            # 最後の石を取らされた
            print("You lose!")
            break

        # 残りの石の数以上の選択肢は削除します
        while total < numbers_to_choose[len(numbers_to_choose)-1]:
            numbers_to_choose.pop(-1)

        # Opponent turn.
        n = get_bestmove()
        print(f"""
  ┌─────┐
  │ ^ ^ │
  │  q  │
  └─┐ ┌─┘
┌───┘ └───┐
│         │ The computer took {n} stone(s).""")
        total -= n

        if total < 1:
            # 最後の石を取らせてやった
            print("You win!")
            break

    # finished.


def create_position_text(total):
    s = """


"""

    for _ in range(0, total):
        s += "o"

    s += """
-------------------------------
         1111111111222222222233
1234567890123456789012345678901
"""

    return s


def get_bestmove():
    """コンピューターの選んだ数"""
    global total, numbers_to_choose

    total_copy = total
    numbers_to_choose_copy = numbers_to_choose[:]

    for choose in numbers_to_choose:
        isWin = playout(choose, total_copy, numbers_to_choose_copy)
        # TODO もっといろいろしたい
        if isWin:
            return choose

    # 適当に選ぶ
    num = random.choice(numbers_to_choose)
    return num


def playout(choose, total_copy, numbers_to_choose_copy):
    # 再帰しなくてもいいや
    while True:
        # Computer turn
        total_copy -= choose
        if total_copy < 1:
            return False

        # 残りの石の数以上の選択肢は削除します
        while total_copy < numbers_to_choose_copy[len(numbers_to_choose_copy)-1]:
            numbers_to_choose_copy.pop(-1)

        # Human turn
        # 適当に選ぶ
        num = random.choice(numbers_to_choose_copy)
        total_copy -= num

        if total_copy < 1:
            return True


if __name__ == "__main__":
    main()
