def params(a=1, b='строка', c=True):
    print(a,b,c)

params()
params(b=25)
params(c=[1,2,3])
params(30)
params('str', 40)

values_list = ['str', False, (1,2,3)]
values_dict = {'a': 35, 'b': True, 'c': set('string') }

params(*values_list)
params(*values_list[2])
params(**values_dict)

values_list2 = [[3,2,], {False}]
params(*values_list2, 42)
params(*values_list2[0], 42)
params(*values_list2[1], 42)