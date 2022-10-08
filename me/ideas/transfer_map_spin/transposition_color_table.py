class TranspositionColorTable:
    """優先する石の色テーブル"""

    def __init__(self):
        self.__table = dict()
        """色テーブル"""

    def add_stonecolor(self, x, y, stonecolor):
        self.__table[hash((x, y))] = stonecolor

    def get_stonecolor(self, x, y):
        return self.__table[hash((x, y))]

    def contains_key(self, x, y):
        return hash((x, y)) in self.__table

    def keys(self):
        return self.__table.keys()
