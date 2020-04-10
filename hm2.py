print("Введите время в секундах: ")
sec = int(input())
hours = (sec % 3600) % 24
minut = (sec - (hours * 3600)) % 60
second = (sec - ((hours * 3600) - (minut * 60)) % 60) % 60

print(str(hours) + ":" + str(minut) + ":" + str(second))
