__author__ = 'Yarlv'
# 08-06-2015

import math

print("Программ решения квадратных уровнений")
print(" a*x^2 + b*x + c = 0")

a = int(input("Введите число, коэффициент a : "))
b = int(input("Введите число, коэффициент b : "))
c = int(input("Введите число, коэффициент с : "))

print("Вариант примера: {0}*x^2 + {1}*x + {2} = 0 .".format(a, b, c, ))

print("D = {0}*{0} − 4*{1}*{2}".format(a, b, c, ))

#Расчёт дискриминанта по фоормуле
# Д = b^2 - 4*a*c
D = math.pow(b, 2) - 4 * a * c

print('D = {0}'.format(D))
if D < 0:
    print('Дискриминант меньше нуля, уровнение не имеет вещественных корней')
else:
    D >= 0
    if D == 0:
        #print('D=0') #Дебаг
        #
        x = (-1 * b )/ 2 * a
        print('Уровнение имеет один корень x = {0}'.format(x))
    else:
        D > 0
        #print('D>0')
        root_1 = (-1 * b + math.sqrt(D)) / 2 * a
        root_2 = (-1 * b - math.sqrt(D)) / 2 * a
        print()
        print('Уровнение имеет два корня: x1 = {0} и x2 = {1}'.format(root_1, root_2,))