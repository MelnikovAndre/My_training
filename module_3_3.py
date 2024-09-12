def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)

print("1.Функция с параметрами по умолчанию:")
print_params(3)
print_params(1,2)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print()
print("2.Распаковка параметров:")
values_list=[23, "лист", True]
values_dict={ 'a' : 23,'b' : 21.45,'c' : False}
values_list = [23, "лист", True]
values_dict = {'a': 23, 'b': 21.45, 'c': False}
print_params(*values_list)
print_params(**values_dict)
print()
print("3.Распаковка + отдельные параметры:")
values_list_2=['Привет',1982]
print_params(*values_list_2, 42)