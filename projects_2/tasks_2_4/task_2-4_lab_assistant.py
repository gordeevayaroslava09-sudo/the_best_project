volume = float(input('Введите массу раствора (в мл): '))
massa = volume * 0.009
water_volume = volume - massa
with open ('recipe.txt', 'w', encoding='utf=8') as file:
    file.write('ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ\n')
    file.write('------------------------------\n')
    file.write(f'Общий объем: {volume: .2f} мл\n')
    file.write(f'Масса соли: {massa: .2f} г \n')
    file.write(f'Объем воды: {water_volume: .2f} мл')