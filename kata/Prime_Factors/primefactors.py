
class PrimeFactors:
    pass

    def of(self, value):
        if value < 2 : return []
        factor = 2
        while value % factor != 0 : factor += 1

        factors = [factor]
        factors.extend(self.of(value/factor))
        return factors

        
