class Conjunto:
    def __init__(self, conjunto):
        self.conjunto = conjunto
    def promedio(self):
        if len(self.conjunto) > 0:
            return sum(self.conjunto) / len(self.conjunto)
        else:
            return None




