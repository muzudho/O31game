import random

numbers_to_choose = []


def main():
    global numbers_to_choose

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
    # 入力を並び替える
    numerics = [str(number) for number in numbers_to_choose]

    total = 31

    while True:
        print(create_position_text(total))

        # Your turn.
        while True:
            try:
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
    global numbers_to_choose
    num = random.choice(numbers_to_choose)
    return num


if __name__ == "__main__":
    main()
