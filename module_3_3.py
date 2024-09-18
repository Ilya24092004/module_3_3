# первая задача
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

# вторая задача
values_list = [1, 'winner', False]
values_dict = {'a' : 1, 'b' : 'two', 'c' : True}

print_params(*values_list)
print_params(**values_dict)

# третья задача

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)
