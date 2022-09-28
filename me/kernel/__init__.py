class Kernel:
    """31game の基本部品"""

    def remove_out_of_range_choices(rest, numbers_to_choose):
        """残りの石の数を超える数の選択肢は削除"""
        while 0 < len(numbers_to_choose) and rest < numbers_to_choose[len(numbers_to_choose)-1]:
            numbers_to_choose.pop(-1)
