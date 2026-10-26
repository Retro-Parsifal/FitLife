water_per_kg = 30  # количество воды в мл на кг веса
ml_in_l = 1000  # количество миллилитров в литре

user_name = input("Добрый день! Как можно к Вам обращаться? ")

try:
    user_age = int(input("Подскажите ваш возвраст? "))
except ValueError:
    print("Пожалуйста, введите корректный возраст использую точку.")
    exit()

try:
    user_weight = float(input("Какой ваш вес (в кг) используя точку - 75.5? "))
except ValueError:
    print("Пожалуйста, введите корректный вес использую точку.")
    exit()

try:
    user_height = float(input("Какой рост (в м) используя точку - 1.8? "))
except ValueError:
    print("Пожалуйста, введите корректный рост использую точку.")
    exit()

bmi = round(user_weight / (user_height ** 2), 1)  # расчёт индекса массы тела

water_ml = user_weight * water_per_kg  # расчет нормы воды в мл
water_l = water_ml / ml_in_l  # преобразование мл в литры

print(f"Отчет для пользователя: {user_name} ({user_age} г.))")
print(f"Твой Индекс Массы Тела: {bmi}")
print(f"Рекомендуемая норма воды: {water_l} л. в день \n")

print("Расчет окончен. Будьте здоровы!\n")
