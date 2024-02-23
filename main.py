from print_answer import PrintAnswer
from average_calc import AverageCalc
from compare_averages import CompareAverages

if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = [3, 2, 1]
    avrg1 = AverageCalc.average_calc(list1)
    avrg2 = AverageCalc.average_calc(list2)
    ANSWER = CompareAverages.compare_averages(avrg1, avrg2)
    PrintAnswer.print_answer(ANSWER)
