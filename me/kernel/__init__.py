class Kernel:
    """31game の基本部品"""

    @staticmethod
    def remove_out_of_range_choices(rest, numbers_to_choose):
        """残りの石の数を超える数の選択肢は削除"""
        while 0 < len(numbers_to_choose) and rest < numbers_to_choose[len(numbers_to_choose)-1]:
            numbers_to_choose.pop(-1)

    def __init__(self):
        """初期化"""

        self.__rest = 0
        """残りの石の個数"""

        self.__numbers_to_choose = []
        """石をいくつ取るかの一覧"""

    @property
    def rest(self):
        """残りの石の個数"""
        return self.__rest

    @rest.setter
    def rest(self, value):
        """残りの石の個数"""
        self.__rest = value

    @property
    def numbers_to_choose(self):
        """石をいくつ取るかの一覧"""
        return self.__numbers_to_choose

    @numbers_to_choose.setter
    def numbers_to_choose(self, value):
        """石をいくつ取るかの一覧"""
        self.__numbers_to_choose = value
