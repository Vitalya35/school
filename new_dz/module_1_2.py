# Напишите 4 переменных которые буду обозначать следующие данные:
# Количество выполненных ДЗ (запишите значение 12)
# Количество затраченных часов (запишите значение 1.5)
# Название курса (запишите значение 'Python')
# Время на одно задание (вычислить используя 1 и 2 переменные)
# Выведите на экран(в консоль), используя переменные, следующую строку:
# Курс: Python, всего задач:12, затрачено часов: 1.5, среднее время выполнения 0.125 часа.

number_of_completed_HT = 12
number_of_hours_spent = 1.5
course_name = 'Python'
time_for_one_task = number_of_hours_spent / number_of_completed_HT
print(f'Курс: {course_name} всего задач: {number_of_completed_HT} затрачено часов: {number_of_hours_spent} среднее времы выполнения: { number_of_hours_spent / number_of_completed_HT}')
print('Курс:', course_name, 'всего задач:', number_of_completed_HT, 'затрачено часов:', number_of_hours_spent, 'среднее время выполнения:', time_for_one_task)
