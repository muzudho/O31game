class TridentHair:
    """三本毛"""

    @staticmethod
    def make(src_point, columns, rows, wa, wb, wc, ha, hb, hc):
        sx = src_point["x"]
        sy = src_point["y"]
        if sx < columns and sy < rows:
            a_point = {"x": sx+wa, "y": sy+ha}
            """次のa点"""

            b_point = {"x": sx+wb, "y": sy+hb}
            """次のb点"""

            c_point = {"x": sx+wc, "y": sy+hc}
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
        return (self.src_point["x"], self.src_point["y"],
                self.a_point["x"], self.a_point["y"],
                self.b_point["x"], self.b_point["y"],
                self.c_point["x"], self.c_point["y"])
