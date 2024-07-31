def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(1, 2, 3)
print_params(b = 25)
print_params(c = [1,2,3])
#######################################
values_list = [2024, 'Bubuka', True]
values_dict = {'a': 2024, 'b': 'Bubuka', 'c': False}
print_params(*values_list)
print_params(**values_dict)
#############################################
values_list_2 = [2024, 'Жаяжая']
print_params(*values_list_2, 42)