def print_params(a = 1, b = 'Строка' ,c = True):
    print(a,b,c)
values_list = [27 ,'лет ', 314]
values_dict = {'a':10, 'b': 20 , 'c':30 }
values_list_2 = [54.32,'Строка']

print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2,42)