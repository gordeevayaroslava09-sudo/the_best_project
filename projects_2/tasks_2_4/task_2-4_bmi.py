weight = float(input("Введите вес (кг): "))
height = float(input("Введите рост (см): "))
bmi = weight / (height ** 2)
print(f"--- Отчет о состоянии здоровья ---\nРост:\t{height} см\nВес:\t{weight} кг\nИндекс массы тела пациента:\t{bmi:.2f}")