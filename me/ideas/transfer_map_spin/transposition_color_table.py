class TranspositionColorTable:
    """優先する石の色テーブル"""

    def __init__(self):
        self.__table = dict()
        """色テーブル"""

    def add_stonecolor(self, point, stonecolor):
        self.__table[hash(point)] = stonecolor

    def get_stonecolor(self, point):
        return self.__table[hash(point)]

    def contains_key(self, point):
        return hash(point) in self.__table

    def keys(self):
        return self.__table.keys()
