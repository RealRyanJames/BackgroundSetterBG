class ConversionColor:
    def __init__(self, r: int):
        self.r = r

    def getColorR(self) -> int:
        return self.r

    def convert(self) -> str:
        return f"{hex(self.getColorR())}"