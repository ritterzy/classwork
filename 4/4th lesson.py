# age = int(input("Сколько тебе лет?"))

# if age >= 18:
#     print("Добро пожаловать!")

# else:
#     if age<= 17:
#      print("Нельзя!")


# age = int(input('Введите возраст:'))
# if 1 <= age <=  10:
#     print("Первая декада")
# elif 21 <= age <= 30:
#     print("Вторая декада")    



# if x / 100 and 4 => невисокосный год
# if x / 100 and 400 => високосный год
# if x / 4 and 400 => високосный
# if x / 100 => невисокосный


year = int(input("Введите год:"))

if year % 400 == 0:
    print("Високосный год!")
elif year % 100 == 0:
    print("Невисокосный!")
elif year % 4 == 0:
    print("Високосный!")
else:
    print("Невисокосный!")  

            