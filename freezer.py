class farm:
    """
    Represent the data of a farm

    attributes: cows, fodder
    """
    def __init__(self, cows, fodder):
        self.cows = cows
        self.fodder = fodder
        self.average_fodder = self.avg_fodder()

    def avg_fodder(self):
        ans = sum(self.fodder)/(365*self.cows)
        return ans

    def __str__(self):
        return f"The farm has {self.cows} cows."

    def __add__(self, other):
        combined_cows = self.cows + other.cows
        return(farm(combined_cows))

    def __call__(self, days):
        ans = self.cows * self.average_fodder * days
        return ans

min_farm = farm(cows, fodder)
fodder_forbrug = min_farm(10)
print(f"Fodder der skal indkøbes til 10 dages forbrug: {fodder_forbrug:.2f} [ton].")