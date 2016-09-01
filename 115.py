__author__ = 'student'
print('Ввод')
a= int(input())
b= ((a-(a % 10))-(a//100)*100)/10
print('Вывод', int(b))