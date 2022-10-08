class TranspositionColorTable:
    """優先する石の色テーブル"""

    def __init__(self):
        self.__table = dict()
        """色テーブル"""

    def add_color(self, n, color):
        self.__table[hash(n)] = color

    def get_color(self, n):
        return self.__table[hash(n)]

    def contains_key(self, n):
        return hash(n) in self.__table

    def keys(self):
        return self.__table.keys()
