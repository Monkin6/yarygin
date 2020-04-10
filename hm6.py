a = int(input())
b = int(input())

r = 10
day = 1
while a <= b:
    a +=(a * r/100)
    day +=1
print("на " + str(day) + "-й день спортсмен достиг результата — не менее 3 км.")