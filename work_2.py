#import - подключение модуля
# должен отдилятся двумя пустыми строчками
#import random
#help(random)
#print(random.randint(1, 6))
#module.method - module_name.method_name
#x = 7
#x % 6
#print(x % 6)

#prefix = "Hi, "
prefix = "Hi"

#print("Hi ", name)
#print('Hi, ', name, sep='')
#print(prefix + name)
# plus для формирования строк некогда не используется
print('{},{}'.format(prefix, name))
#format(prefix, name)) - переменные
# колво скобок слева - должны соответствовать аргументам (как тут, префикс, нейм)