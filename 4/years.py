age = int(input("Введите возраст"))

if(age>=21):
    b = age-21
    d = b/4 + 2
elif(age<21):
    a = age/10.5
    d = a
elif(age<0):
    print("ошибка!")
print(d)    


