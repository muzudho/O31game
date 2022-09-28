import random
from kernel import Kernel


class Think:

    @staticmethod
    def get_bestmove(rest, numbers_to_choose):
        """コンピューターの選んだ数"""

        win_count = [0] * len(numbers_to_choose)
        lose_count = [0] * len(numbers_to_choose)

        # TODO もっといろいろ思考したい
        playout_try_count = 50000  # プレイアウト回数。数字は適当
        for _ in range(0, playout_try_count):
            # 適当に選ぶ
            index = random.randint(0, len(numbers_to_choose)-1)
            number_taken = numbers_to_choose[index]

            numbers_to_choose_copy = numbers_to_choose[:]  # 配列はスライスを渡す
            isWin = Think.playout(number_taken, rest, numbers_to_choose_copy)
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

    @staticmethod
    def playout(number_taken, rest, numbers_to_choose):
        # 再帰しなくてもいいや
        while True:
            # Computer turn
            rest -= number_taken
            if rest < 1:
                # コンピューターが全部の石を取ったら、コンピューターの勝ち
                return True

            # 残りの石の数以上の選択肢は削除します
            Kernel.remove_out_of_range_choices(rest, numbers_to_choose)

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
            Kernel.remove_out_of_range_choices(rest, numbers_to_choose)

            if len(numbers_to_choose) < 1:
                # FIXME コンピューターに、選べる選択肢を残さなかったら、コンピューターの負け
                return False
