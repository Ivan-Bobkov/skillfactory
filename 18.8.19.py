amount = 0
ticket = (int(input("Введите количество билетов:")))
for age in range(ticket):
    age = (int(input("Введите возраст посетителя:")))
    if age < 18:
        amount += 0
    elif age >= 18 and age <= 25:
        amount += 990
    elif age > 25:
        amount += 1390
if ticket > 3:
    amount -= amount / 100 * 10
print("Стоимость Ваших билетов", amount)
