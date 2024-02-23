class AverageCalc:

    @staticmethod
    def average_calc(lst):
        if not lst:
            return 0
        return sum(lst) / len(lst)
