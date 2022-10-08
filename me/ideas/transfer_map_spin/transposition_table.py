class TranspositionTable:
    """合流テーブル"""

    def __init__(self):
        self.__transposition_table = dict()

    @property
    def table(self):
        return self.__transposition_table

    def add_trident(self, hash_key, trident):
        self.__transposition_table[hash_key] = trident
