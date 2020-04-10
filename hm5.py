revenue = int(input())
cost = int(input())
if revenue > cost:
    print("прибыль — выручка больше издержек")
    profitably = (revenue / cost) * 100
    print(int(profitably))
    print("ведите количесво работников")
    people = int(input())
    people_fin = revenue / people
    print(people_finp)
else:
    print("убыток — издержки больше выручки")
