class TranspositionTable:
    """合流テーブル"""

    def __init__(self):
        self.__table = dict()
        """合流テーブル"""

    def add_trident(self, hash_key, trident):
        self.__table[hash_key] = trident

    def get_trident(self, hash_key):
        return self.__table[hash_key]

    def contains_key(self, hash_key):
        return hash_key in self.__table

    def keys(self):
        return self.__table.keys()

    def values(self):
        return self.__table.values()
