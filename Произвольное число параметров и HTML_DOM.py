def test(n, *x, txt1="яблок съели", txt2="поделившись с", a):
    print(n, txt1,*x,txt2,a)

b = {'a': 'Александрой'}
c = {'a':'Евгенией'}
y =['Коля и Маша','Петя и Даша']
test(5,y[0], **b)
test(6,y[1],txt1='груш съели',**c)

def fak(n):
    if n == 1:
        return 1
    else:
        return fak(n - 1) * n

print(fak(5))