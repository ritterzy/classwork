# starting_hours = int(input("Введите часы:"))
# starting_mins = int(input("введите минуты:"))


# delta_hours = int(input("Укажите разницу hour:"))
# delta_mins = int(input("Укажите разницу min:"))

# hours = (starting_hours + delta_hours)% 24
# minutes =(starting_mins + delta_mins)% 60

# if minutes < 10:
#     minutes = "0" + str(minutes)

# if hours < 10:
#     hours = "0" + str(hours)

# print(f'{hours} : {minutes}')

total_num = int(input("Количество:"))
floors = int(input("Сколько этажей:"))
apart = int(input("Номер квартиры:"))
if apart<= 0:
    print("Error")
elif apart > total_num:
    print("Error")
elif floors <=0:
    print("Error")
elif total_num % floors !=0:
     print("Error")

else:
    nomer_etaja = apart / (total_num / floors) + 0.49
    print("Вы живёте на " + str(round(nomer_etaja)) + " " + "этажей")