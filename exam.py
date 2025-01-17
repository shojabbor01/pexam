# task1
# Як комбайн A тонна ғалла даравид, ва дуюмаш B тонна камтар. Ҳар ду комбайн чӣ қадар ғалла даравиданд?

# **Input**
# ```
# A = 34
# B = 10
# ```
# **Output**
# ```
# 58
# **Шарҳ:**
# - Комбайни якум 34 тонна даравид
# - Комбайни дуюм: 34 - 10 = 24 тонна даравид
# - Ҳамагӣ: 34 + 24 = 58 тонна

# k1 = int(input())
# k2 = int(input())
# k3 = k1-k2
# print(k1+k3)




#task 2
# В автобусе было A пассажиров. На остановке вышло B пассажиров и вошло C. Сколько пассажиров стало в автобусе?

# ----

# Дар автобус A мусофир буд. Дар истгоҳ B мусофир фаромад ва C мусофир даромад. Дар автобус чанд мусофир шуд?

# **Input**
# ```
# A = 53
# B = 12
# C = 18
# ```
# **Output**
# ```
# 59
# ```
# **Объяснение:**
# - Изначально было 53 пассажира
# - Вышло 12 пассажиров: 53 - 12 = 41
# - Вошло 18 пассажиров: 41 + 18 = 59
# Итоговое количество пассажиров: 59

# ----

# **Шарҳ:**
# - Аввал 53 мусофир буд
# - 12 мусофир фаромад: 53 - 12 = 41
# - 18 мусофир даромад: 41 + 18 = 59
# Шумораи ниҳоии мусофирон: 59

# k1 = int(input())
# k2 = int(input())
# k3 = int(input())
# k3 = (k1-k2)+k3
# print(k3)



#task3

# Дано четырехзначное число. Найдите максимальную цифру в этом числе.

# ----

# Адади чорхонагӣ дода шудааст. Рақами калонтаринро дар ин адад ёбед.

# **Input**
# ```
# The number is: 1502
# ```
# **Output**
# ```
# Max = 5

# **Объяснение:**
# В числе 1502:
# - Цифры: 1, 5, 0, 2
# - Максимальная цифра - 5

# ----

# **Шарҳ:**
# Дар адади 1502:
# - Рақамҳо: 1, 5, 0, 2
# - Рақами калонтарин - 5

# a = int(input())
# n1 = a//1000
# n2 = a//100%10
# n3 = a//10%10
# n4 = a%10
# print(max(n1,n2,n3,n4))


#task4

# Даны четыре целых числа. Найдите количество положительных, отрицательных чисел и количество нулей в исходном наборе.

# ----

# Чор адади бутун дода шудааст. Шумораи ададҳои мусбӣ, манфӣ ва сифрҳоро дар маҷмӯи ибтидоӣ ёбед.

# **Input**
# ```
# number1: 2
# number2: 3
# number3: -3
# number4: 0
# ```
# **Output**
# ```
# Number of positive: 2
# Number of negative: 1
# Number of zeros: 1
# ```
# **Объяснение:**
# - Положительные числа: 2, 3 (количество: 2)
# - Отрицательные числа: -3 (количество: 1)
# - Нули: 0 (количество: 1)

# ----

# **Шарҳ:**
# - Ададҳои мусбӣ: 2, 3 (миқдор: 2)
# - Ададҳои манфӣ: -3 (миқдор: 1)
# - Сифрҳо: 0 (миқдор: 1)

# k1 = int(input())
# k2 = int(input())
# k3 = int(input())
# k4 = int(input())
# cnt1=0
# cnt2=0
# cnt3=0

# if k1>0:
#     cnt1+=1
# if k2>0:
#     cnt1+=1
# if k3>0:
#     cnt1+=1
# if k4>0:
#     cnt1+=1
# print("Number of positive: ", cnt1)
# if k1<0:
#     cnt2+=1
# if k2<0:
#     cnt2+=1
# if k3<0:
#     cnt2+=1
# if k4<0:
#     cnt2+=1
# print("Number of negative: ", cnt2)
# if k1==0:
#     cnt3+=1
# if k2==0:
#     cnt3+=1
# if k3==0:
#     cnt3+=1
# if k4==0:
#     cnt3+=1 
# print("Number of zeros: ", cnt3)
       


#task5

# Напишите программу для отображения следующего и предыдущего четного числа для заданного числа.

# ----

# Барномае нависед, ки адади ҷуфти навбатӣ ва пешинаро барои адади додашуда нишон диҳад.

# **Input**
# ```
# The number is: 150
# ```
# **Output**
# ```
# The next number for the number 150 is 152
# The previous number for the number 150 is 148
# ```

# **Объяснение:**
# Для числа 150:
# - Следующее четное число: 152 (150 + 2)
# - Предыдущее четное число: 148 (150 - 2)

# ----

# **Шарҳ:**
# Барои адади 150:
# - Адади ҷуфти навбатӣ: 152 (150 + 2)
# - Адади ҷуфти пешина: 148 (150 - 2)

# n = int(input())
# print(f"The next number for the number {n} is {n+(n%2==0)+1}\nThe previous number for the number {n} is {n+(n%2!=0)-2}")


#task 6

# Дано пятизначное число. Найдите сумму и произведение его цифр.

# ----

# Адади панҷхонагӣ дода шудааст. Сумма ва ҳосили зарби рақамҳои онро ёбед.

# **Input**
# ```
# 19283
# ```
# **Output**
# ```
# The sum of the digits is: 1+9+2+8+3 = 23
# The product of the digits is: 1*9*2*8*3 = 432
# ```
# **Объяснение:**
# Для числа 19283:
# - Сумма: 1 + 9 + 2 + 8 + 3 = 23
# - Произведение: 1 × 9 × 2 × 8 × 3 = 432

# ----

# **Шарҳ:**
# Барои адади 19283:
# - Сумма: 1 + 9 + 2 + 8 + 3 = 23
# - Ҳосили зарб: 1 × 9 × 2 × 8 × 3 = 432

# a = int(input())
# n1 = a//10000
# n2 = a//1000%10
# n3 = a//100%10
# n4 = a//10%10
# n5 = a%10
# print(f"Сумма: {n1}+{n2}+{n3}+{n4}+{n5}={n1+n2+n3+n4+n5}\nҲосили зарб: {n1}x{n2}x{n3}x{n4}x{n5}={n1*n2*n3*n4*n5}")


#task7

# Напишите программу для отображения n членов натурального ряда чисел и их суммы.

# ----

# Барномае нависед, ки n ҷумлаи ададҳои натуралӣ ва суммаи онҳоро нишон диҳад.

# **Input**
# ```
# Input a number of terms: 7
# ```
# **Output**
# ```
# The natural numbers up to 7th terms are: 1 2 3 4 5 6 7
# The sum of the natural numbers is: 28


# **Объяснение:**
# - Первые 7 натуральных чисел: 1, 2, 3, 4, 5, 6, 7
# - Их сумма: 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28

# ----

# **Шарҳ:**
# - 7 адади аввали натуралӣ: 1, 2, 3, 4, 5, 6, 7
# - Суммаи онҳо: 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28

# n = int(input())
# sum = 0
# i = 0
# while i<n:
#     i+=1
#     sum+=i    
#     print(i, end=" ")   
# print()    
# print(f"The sum of the natural numbers is: {sum}")




#task 8

# Дано вещественное число — цена 1 кг конфет. Вывести стоимость 1, 2, ..., 10 кг конфет.

# ----

# Адади ҳақиқӣ — нархи 1 кг қанд дода шудааст. Арзиши 1, 2, ..., 10 кг қандро нишон диҳед.

# **Input**
# ```
# Cost: 5.50
# ```
# **Output**
# ```
# 1 kg – 5.5
# 2 kg – 11
# 3 kg – 16.5
# 4 kg – 22
# 5 kg – 27.5
# 6 kg – 33
# 7 kg – 38.5
# 8 kg – 44
# 9 kg – 49.5
# 10 kg – 55
# ```

# **Explanation:**
# Price calculation for each kilogram:
# - 1 kg: 5.50 × 1 = 5.50
# - 2 kg: 5.50 × 2 = 11.00
# And so on...

# ----

# **Объяснение:**
# Расчет стоимости для каждого килограмма:
# - 1 кг: 5.50 × 1 = 5.50
# - 2 кг: 5.50 × 2 = 11.00
# И так далее...

# ----

# **Шарҳ:**
# Ҳисоби нарх барои ҳар як килограмм:
# - 1 кг: 5.50 × 1 = 5.50
# - 2 кг: 5.50 × 2 = 11.00
# Ва ғайра...


# n = int(input())
# j = 0
# i=1
# while i<=n:
#     j+=1   
#     print(f"{j} kg - {i*n}") 
#     i=i+1


### Task 9
# Write a program to find the factorial of a number.

# ----

# Напишите программу для нахождения факториала числа.

# ----

# Барномае нависед, ки факториали ададро ёбад.

# **Input**
# ```
# Input a number to find the factorial: 5
# ```
# **Output**
# ```
# The factorial of the given number is: 120
# ```

# **Explanation:**
# 5! = 5 × 4 × 3 × 2 × 1 = 120

# ----

# **Объяснение:**
# 5! = 5 × 4 × 3 × 2 × 1 = 120

# ----

# **Шарҳ:**
# 5! = 5 × 4 × 3 × 2 × 1 = 120

# n = int(input())
# i=1
# fact = 0
# while i<=n:
#     fact=i*i
#     i+=1
#     print(fact)
# print("The factorial of the given number is: ", fact)    