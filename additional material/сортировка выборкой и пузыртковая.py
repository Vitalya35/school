def bubble_sort(ls):   # пузырьковая сортировка
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(ls) - 1):
            if ls[i] > ls[i+1]:
                ls[i], ls[i+1] = ls[i+1], ls[i]
                swapped = True
    return print(ls)


def selection_sort(ls):  # сортировка выборкой
    for i in range(len(ls)):
        lowest = i
        for j in range(i + 1, len(ls)):
            if ls[j] < ls[lowest]:
                lowest = j
        ls[i], ls[lowest] = ls[lowest], ls[i]
    return print(ls)


