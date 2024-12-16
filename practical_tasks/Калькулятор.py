import tkinter as tk
# пару полезных функций и любимый цвет для жены, которая работает бугалтером.
def get_values():
    num1 = float(number1_entry.get())
    num2 = float(number2_entry.get())
    return num1, num2

def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)

def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)

def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)

def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)

def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)

def NDS():
    num1 = float(number1_entry.get())
    res = round(num1 * 20 / 120, 2)
    insert_values(res)

def X():
    num1 = float(number1_entry.get())
    res = round(num1 * 100 / 87, 2)
    insert_values(res)

window = tk.Tk()
window.title('Зайкины cчёты')
window.geometry('300x270+1050+400')
window.resizable(False, False)
window.configure(background='aquamarine2')
button_add = tk.Button(window, text='+', width=2, height=2, command=add)
button_add.place(x=60, y=125)
button_sub = tk.Button(window, text='-', width=2, height=2, command=sub)
button_sub.place(x=90, y=125)
button_mul = tk.Button(window, text='*', width=2, height=2, command=mul)
button_mul.place(x=120, y=125)
button_div = tk.Button(window, text='/', width=2, height=2, command=div)
button_div.place(x=150, y=125)
button_nds = tk.Button(window, text='НДС', width=3, height=2, command=NDS)
button_nds.place(x=180, y=125)
button_X = tk.Button(window, text='X', width=2, height=2, command=X)
button_X.place(x=218, y=125)
number1_entry = tk.Entry(window, width=28)
number1_entry.place(x=65, y=30)
number2_entry = tk.Entry(window, width=28)
number2_entry.place(x=65, y=80)
answer_entry = tk.Entry(window, width=28)
answer_entry.place(x=65, y=205)
number1 = tk.Label(window, text='Первое число(поле для НДС, X)', background='aquamarine2')
number1.place(x=60, y=5)
number2 = tk.Label(window, text='Второе число', background='aquamarine2')
number2.place(x=110, y=55)
answer = tk.Label(window, text='Ответ', background='aquamarine2')
answer.place(x=135, y=180)
window.mainloop()
