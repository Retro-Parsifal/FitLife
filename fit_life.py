user_name = input("Добрый день! Как можно к Вам обращаться? ")
user_age = int(input("Подскажите ваш возвраст? "))

user_weight = float(input("Какой ваш вес (в кг) например 75.5? "))
user_height = float(input("Какой рост (в м) например 1.8? "))

bmi = round(user_weight / (user_height ** 2), 1)  # расчёт индекса массы тела

water_ml = user_weight * 30  # расчет нормы воды в мл
water_l = water_ml / 1000  # преобразование мл в литры

print(f"Отчет для пользователя: {user_name} ({user_age} г.))")
print(f"Твой Индекс Массы Тела: {bmi}")
print(f"Рекомендуемая норма воды: {water_l} л. в день \n")

print("Расчет окончен. Будьте здоровы!\n")