immutable_var = ('Aleksandra', ['Valeriya', 'Nellya'], 123,123)
print(immutable_var)
 # immutable_var[0] = ('viktoriya')
mutable_list = ['fibonachi', 5,8,13,21]
print(mutable_list )
mutable_list.append(34)
print(mutable_list)
mutable_list.extend([55,'from Pisa'])
print(mutable_list)
mutable_list.remove(5)
print(mutable_list)
print(mutable_list[0:7:6])