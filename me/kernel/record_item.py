class RecordItem:
    """棋譜の要素"""

    def __init__(self, number_taken, removed_chooses):
        self.__number_taken = number_taken
        self.__removed_chooses = removed_chooses

    @property
    def number_taken(self):
        return self.__number_taken

    @property
    def removed_chooses(self):
        return self.__removed_chooses
