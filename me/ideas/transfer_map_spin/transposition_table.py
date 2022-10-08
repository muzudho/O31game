class TranspositionTable:
    """合流テーブル"""

    def __init__(self):
        self.__transposition_table = dict()

    @property
    def table(self):
        return self.__transposition_table

    def add_trident(self, hash_key, trident):
        self.__transposition_table[hash_key] = trident

    def get_trident(self, hash_key):
        return self.__transposition_table[hash_key]

    def contains_key(self, hash_key):
        return hash_key in self.__transposition_table

    def keys(self):
        return self.__transposition_table.keys()
