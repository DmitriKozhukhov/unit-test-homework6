class CompareAverages:

    @staticmethod
    def compare_averages(avrg1, avrg2):
        if avrg1 > avrg2:
            return "Первый список имеет большее среднее значение"
        if avrg1 < avrg2:
            return "Второй список имеет большее среднее значение"
        if avrg1 == avrg2:
            return "Средние значения равны"
