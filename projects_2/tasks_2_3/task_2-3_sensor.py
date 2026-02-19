name = input('Введите имя оператора: ')
meaning = input('Введите значение датчика давления: ')
with open('sensor_log.txt', 'w', encoding='utf-8') as sensor:
    sensor.write(f'Оператор {name}\t')
    sensor.write(f'{meaning}')
print('Данные успешно сохранены в sensor_log.txt')