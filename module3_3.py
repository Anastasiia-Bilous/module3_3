def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print()

values_list = [5,'hello', True]
print_params(*values_list)

values_dict = {'a':100,'b':'y','c':'Dik'}
print_params(**values_dict)

values_list_2 = [500,'Kim']
print_params(*values_list_2,42)





