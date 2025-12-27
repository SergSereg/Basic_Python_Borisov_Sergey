# #======================================
# # 1. Создание переменных и вывод значений
# #======================================
# name = "Сергей"
# age = 36
# height = 181.1
# # Вывод с поясняющими подписями
# print(f"Имя: {name}")
# print(f"Возраст: {age} лет")
# print(f"Рост: {height} см")

# #======================================
# # Какой вариант лучше?
# # 2. Изменение значений переменных (1 Вариант)
# #======================================
# x = 10
# print(type(x))
# x = 25.5
# print(type(x))
# x = "Python"
# print(type(x))
# print(x)
# # 2. Изменение значений переменных (2 Вариант)
# x = 10
# print(f"{type(x)}")
# x = 25.5
# print(f"{type(x)}")
# x = "Python"
# print(f"{type(x)}")
# print(x)

# #======================================
# # 3. Копирование ссылок
# #======================================
# a = 7    # a → ссылается на объект 7
# b = a    # b → ссылается туда же: на объект 7, Теперь a и b — две метки на ОДИН объект (7)
# print(a)
# print(b)
# print(id(a), id(b))
# a = 10   # a → отцепляется от 7 и цепляется к НОВОМУ объекту — 10
# print(a)
# print(b) # b всё ещё ссылается на старый объект — 7
# print(id(a), id(b))

# #======================================
# # 4. Каскадное присваивание
# #======================================
# x = y = z = 100  # Каскадное присваивание: x, y, z = 100
# print(x)
# print(y)
# print(z)
# print(id(x))
# print(id(y))
# print(id(z))
# x, y, z = 1, 2, 3 # Множественное присваивание: разные значения
# print(x)
# print(y)
# print(z)
# print(id(x))
# print(id(y))
# print(id(z))

# #======================================
# # 5. Обмен значений переменных
# #======================================
# a = 5
# b = 10
# a, b = b, a  # Обмениваем значения с помощью множественного присваивания
# print(a)
# print(b)

# #======================================
# # 6. Работа с именами переменных
# #======================================
# True = 5        # ❌ SyntaxError: cannot assign to keyword
# if = 10         # ❌ SyntaxError: invalid syntax
# print = "test"  # ⚠️ print — встроенная функция, а не ключевое слово.
# import keyword
# print(keyword.kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
#  'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally',
#  'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
#  'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# #======================================
# # 7. Использование функции type()
# #======================================
# var1 = 42
# var2 = 3.14
# var3 = "Hello"
# print(type(var1))
# print(type(var2))
# print(type(var3))
# var1 = "World" # Присваиваем var1 строковое значение
# print(type(var1))

# #======================================
# # 8. Дополнительные задания
# #======================================
username = "sergey"
age = 36
height_m = 1.81
is_student = False
score = 95.5
# Вывод значений и типов
print(username)
print(type(username))

print(age)
print(type(age))

print(height_m)
print(type(height_m))

print(is_student)
print(type(is_student))

print(score)
print(type(score))

# Переменная с русским именем
результат = 42
print(результат)
print(type(результат))

result = f"Age: {25}"
print(result)