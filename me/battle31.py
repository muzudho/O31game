# Author: Muzudho

import random
from kernel import Kernel
from kernel.scenes import Scenes

# このゲームの基本部品
kernel = Kernel()

# 残りの石の個数
rest = 0

numbers_to_choose = []


def main():
    global kernel, rest, numbers_to_choose

    # Title
    print(Scenes.stringify_title())

    # 山にいくつ石がありますか？
    while True:
        # [Ctrl]+[C]キーで抜けたいので、input を try 句の外に出します
        enter = input(
            Scenes.stringify_how_many_stones_there_in_there_heap())

        try:
            if enter == "exit" or enter == "quit":
                print("Bye.")
                exit(0)

            rest = int(enter)
            break

        except:
            print("Please try again!")

    # 取っていい石の数（複数）
    while True:
        # [Ctrl]+[C]キーで抜けたいので、input を try 句の外に出します
        enter = input(
            Scenes.stringify_how_many_do_you_want_to_take_at_one_time())

        try:
            if enter == "exit" or enter == "quit":
                print("Bye.")
                exit(0)

            numerics = enter.split(",")
            numbers_to_choose = [int(numeric) for numeric in numerics]
            # 昇順ソート
            numbers_to_choose.sort()
            print(Scenes.stringify_position_text(rest, 0))
            break

        except:
            print("Please try again!")

    while True:

        # 残りの石の数以上の選択肢は削除します
        remove_out_of_range_choices(rest, numbers_to_choose)

        # Your turn.

        if len(numbers_to_choose) < 1:
            # まだ石が残っているのに、選択肢がない
            print(Scenes.stringify_you_lose_stone_remaining())
            break

        while True:
            # 入力を並び替える
            numerics = [str(number) for number in numbers_to_choose]
            choose = " ".join(numerics)

            # [Ctrl]+[C]キーで抜けたいので、input を try 句の外に出します
            enter = input(Scenes.stringify_how_many_do_you_take(choose))

            try:
                if enter == "exit" or enter == "quit":
                    print("Bye.")
                    exit(0)

                number_taken = int(enter)

                # 選択肢の中からちゃんと選んだら
                if number_taken in numbers_to_choose:
                    # ループから抜ける
                    break

                print("Please try again!")

            except:
                print("Please try again!")

        rest -= number_taken
        print(Scenes.stringify_position_text(rest, number_taken))

        if rest < 1:
            # 最後の石を取った
            print(Scenes.stringify_you_win_stone_none())
            break

        # 残りの石の数以上の選択肢は削除します
        remove_out_of_range_choices(rest, numbers_to_choose)

        # Opponent turn.

        if len(numbers_to_choose) < 1:
            # まだ石が残っているのに、選択肢がないなら、コンピューターの負け
            print(Scenes.stringify_you_win_stone_remaining())
            break

        number_taken = get_bestmove()

        print(Scenes.stringify_computer_took_some_stones(number_taken))
        rest -= number_taken
        print(Scenes.stringify_position_text(rest, number_taken))

        if rest < 1:
            # 最後の石を取られた
            print(Scenes.stringify_you_lose_stone_none())
            break

    # finished.


def get_bestmove():
    """コンピューターの選んだ数"""
    global rest, numbers_to_choose

    win_count = [0] * len(numbers_to_choose)
    lose_count = [0] * len(numbers_to_choose)

    # TODO もっといろいろ思考したい
    playout_try_count = 50000  # プレイアウト回数。数字は適当
    for _ in range(0, playout_try_count):
        # 適当に選ぶ
        index = random.randint(0, len(numbers_to_choose)-1)
        choose = numbers_to_choose[index]

        numbers_to_choose_copy = numbers_to_choose[:]  # 配列はスライスを渡す
        isWin = playout(choose, rest, numbers_to_choose_copy)
        if isWin:
            win_count[index] += 1
        else:
            lose_count[index] += 1

    # 勝率が一番高かった手を選ぶ
    high_rate = 0
    high_index = -1
    for index in range(0, len(numbers_to_choose)):
        rest_num = win_count[index] + lose_count[index]
        if 0 < rest_num:
            rate = win_count[index]/rest_num

            # info
            print(
                f"[{numbers_to_choose[index]:2}] {rate:1.2f} = {win_count[index]}/{rest_num}")

            if high_rate < rate:
                high_rate = rate
                high_index = index

    return numbers_to_choose[high_index]


def playout(choose, rest, numbers_to_choose):
    # 再帰しなくてもいいや
    while True:
        # Computer turn
        rest -= choose
        if rest < 1:
            # コンピューターが全部の石を取ったら、コンピューターの勝ち
            return True

        # 残りの石の数以上の選択肢は削除します
        remove_out_of_range_choices(rest, numbers_to_choose)

        if len(numbers_to_choose) < 1:
            # FIXME 相手に、選べる選択肢を残さなかったら、こっちの勝ち
            return True

        # Human turn
        # 適当に選ぶ
        num = random.choice(numbers_to_choose)
        rest -= num

        if rest < 1:
            # 人間が全部の石を取ったら、コンピューターの負け
            return False

        # 残りの石の数以上の選択肢は削除します
        remove_out_of_range_choices(rest, numbers_to_choose)

        if len(numbers_to_choose) < 1:
            # FIXME コンピューターに、選べる選択肢を残さなかったら、コンピューターの負け
            return False


def remove_out_of_range_choices(rest, numbers_to_choose):
    """残りの石の数を超える数の選択肢は削除"""
    while 0 < len(numbers_to_choose) and rest < numbers_to_choose[len(numbers_to_choose)-1]:
        numbers_to_choose.pop(-1)


if __name__ == "__main__":
    main()
