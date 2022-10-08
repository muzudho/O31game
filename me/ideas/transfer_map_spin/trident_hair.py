class TridentHair:
    """三本毛

    - 始点の石の色は含みません。始点の位置は含みます"""

    @staticmethod
    def make(src_point, columns, rows, a, b, c, ha, hb, hc):
        sx = src_point[0]
        sy = src_point[1]
        if sx < columns and sy < rows:
            a_point = (sx+a, sy+ha)  # x, y
            """次のa点"""

            b_point = (sx+b, sy+hb)
            """次のb点"""

            c_point = (sx+c, sy+hc)
            """次のc点"""

            return TridentHair(src_point, a_point, b_point, c_point)

        return None

    def __init__(self, src_point, a_point, b_point, c_point):
        self.__src_point = src_point
        self.__a_point = a_point
        self.__b_point = b_point
        self.__c_point = c_point

    @property
    def src_point(self):
        """始点"""
        return self.__src_point

    @property
    def a_point(self):
        """a線の終点"""
        return self.__a_point

    @property
    def b_point(self):
        """b線の終点"""
        return self.__b_point

    @property
    def c_point(self):
        """c線の終点"""
        return self.__c_point

    def create_hash(self):
        return (self.src_point[0], self.src_point[1],  # x, y
                self.a_point[0], self.a_point[1],
                self.b_point[0], self.b_point[1],
                self.c_point[0], self.c_point[1])
