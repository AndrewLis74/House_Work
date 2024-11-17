def print_params(a = 1,b = 'строка',c = True):
    print(a,b,c)
print_params(2)
print_params(3,2)
print_params(4,2,3)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])
def print_params_1(a = 1,b = 'строка',c = True):
    print(a,b,c)
value_list = [ 1,'string',False]
print_params_1(*value_list)
def print_params_2(a = 1,b = 'строка',c = True):
    print(a,b,c)
values_dict = {'a': 2, 'b': 'string', 'c': True}
print_params_2(**values_dict)
def print_params_3(a = 1,b = 'строка',c = True):
    print(a,b,c)
value_list_2 = [25.14, 'строка']
print_params_3(*value_list_2,42)




