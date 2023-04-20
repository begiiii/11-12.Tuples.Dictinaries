'''
Задание №1.
Написать лямбду-функцию, которая:
1. добавляет 15 к заданному числу, переданному в качестве аргумента;
Input: 10 Output:25
2. умножает аргумент x на аргумент y, выведите результат;
Input: 12 4 Output:48
3. фильтрует список целых чисел, заданных пользователем;
Список целых чисел:
[78, 2, 13, 46, 5, 61, 74, 81, 94, 10]
Список четных чисел:
[78, 2, 46, 74, 94, 10]
Список нечетных чисел:
[13, 5, 61, 81]
'''

add15 = lambda x: x+15
print('add15() : ', add15(10))

mult = lambda x,y: x*y 
print('mult() : ', mult(1,5))

lst=[-4,56,98,-52,963,-741,-25,8]
print("Список целых чисел: ", list(filter(lambda n:n>0,lst)))
print("Список нечетных чисел: ", list(filter(lambda n:n%2==0,lst)))
print("Список нечетных чисел: ", list(filter(lambda n:n%2!=0,lst)))



