
s = [1, 2, 3, 4]                                # СПИСКОВЫЕ ВКЛЮЧЕНИЯ
                                             # с помощью цикла фор умножить список чисел на 2, в одну строку.
def dubler(lst):
    return print([i * 2 for i in lst])
    # return print([i * 2 for i in lst if i % 2 == 0])    # умножить четные
    # return print([i for i in lst if i % 2 == 0])   # вычленить четные
    # spisok = []
    # for i in lst:
    #     spisok.append(i * 2)
    # return print(spisok)

dubler(s)