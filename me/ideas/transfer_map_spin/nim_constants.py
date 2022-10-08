class NimConstants:
    __stonecolor_x = 0
    """グランディ数0の石の色"""

    __stonecolor_a = 1
    """a石の色"""

    __stonecolor_b = 2
    """b石の色"""

    __stonecolor_c = 3
    """c石の色"""

    @property
    def stonecolor_x(self):
        """グランディ数0の石の色"""
        return self.__stonecolor_x

    @property
    def stonecolor_a(self):
        """a石の色"""
        return self.__stonecolor_a

    @property
    def stonecolor_b(self):
        """b石の色"""
        return self.__stonecolor_b

    @property
    def stonecolor_c(self):
        """c石の色"""
        return self.__stonecolor_c


nim_constants = NimConstants()
