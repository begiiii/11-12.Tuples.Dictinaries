

#Задачи по теме "Работа со словарями"

#1) Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь, 
#в котором каждый элемент списка является и ключом и значением. Предполагается, что элементы списка 
#будут соответствовать правилам задания ключей в словарях.

lst = [1,2,3,"uyghbd"]

def to_dict(lst):
    return {a: a for a in lst}

print("to_dict(lst) : ", to_dict(lst))

#2) Иван решил создать самый большой словарь в мире. Для этого он придумал функцию biggest_dict(**kwargs), 
#которая принимает неограниченное количество параметров «ключ: значение» и обновляет 
#созданный им словарь my_dict, состоящий всего из одного элемента «first_one» со значением 
#«we can do it». Воссоздайте эту функцию.


def biggest_dict(biggestDictionary, **kwargs):
    for key, value in kwargs.items():
        biggestDictionary[key] = value
    return biggestDictionary

biggestDictionary = {"first_one" : "we can do it"}

print("biggest_dict() : ", biggest_dict(biggestDictionary, bob="name", sa="sc"))


#3) Дана строка в виде случайной последовательности чисел от 0 до 9. 
#Требуется создать словарь, который в качестве ключей будет принимать 
#данные числа (т. е. ключи будут типом int), а в качестве значений – 
#количество этих чисел в имеющейся последовательности. Для построения
# словаря создайте функцию count_it(sequence), принимающую строку из
#  цифр. Функция должна возвратить словарь из 3-х самых часто встречаемых чисел.


def count_it(sequence):
    myDict = {}
    for item in sequence:
        if item not in myDict:
            myDict[int(item)] = 1
        else:
            myDict[int(item)] = myDict[item] + 1
            

    #myDict.items() - список кортежей

    #сортирем по value и через срез выбираем первые 3
    sortedDict = sorted(myDict.items(), key=lambda item: item[1], reverse=True)[:3]

    return dict(sortedDict)

print('count_it() : ', count_it('1111563677363626722233333'))
            



#4) Создайте словарь с количеством элементов не менее 5-ти. 
#Поменяйте местами первый и последний элемент объекта. 
#Удалите второй элемент. Добавьте в конец ключ «new_key» со 
#значением «new_value». Выведите на печать итоговый словарь.
# Важно, чтобы словарь остался тем же (имел тот же адрес в памяти).

myDict = {1:5,2:5,3:1,4:7,5:3}
print("myDict before : ", myDict)

first = list(myDict.keys())[0]
last = list(myDict.keys())[-1]

myDict[first], myDict[last] = myDict[last], myDict[first]


myDict.pop(list(myDict.keys())[1])

#del myDict[list(myDict.keys())[1]]


#myDict["new_key"] = "new_value"
myDict.update({"new_key" : "new_value"})

print("myDict after : ", myDict)


