# Author: Muzudho

from kernel import Kernel
from kernel.scenes import Scenes
from kernel.think import Think

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
        Kernel.remove_out_of_range_choices(rest, numbers_to_choose)

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
        Kernel.remove_out_of_range_choices(rest, numbers_to_choose)

        # Opponent turn.

        if len(numbers_to_choose) < 1:
            # まだ石が残っているのに、選択肢がないなら、コンピューターの負け
            print(Scenes.stringify_you_win_stone_remaining())
            break

        number_taken = Think.get_bestmove(rest, numbers_to_choose)

        print(Scenes.stringify_computer_took_some_stones(number_taken))
        rest -= number_taken
        print(Scenes.stringify_position_text(rest, number_taken))

        if rest < 1:
            # 最後の石を取られた
            print(Scenes.stringify_you_lose_stone_none())
            break

    # finished.


if __name__ == "__main__":
    main()
