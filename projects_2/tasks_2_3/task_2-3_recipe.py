name_of_nutrient_medium = input('Введите название питательной среды: ')
agar_concentration = input('Введите концентрацию агара(%): ')
sterilization_temperature = input('Введите температуру стерилизации: ')
with open('recipe.txt', 'w', encoding='utf-8') as recipe:
    recipe.write(f'{name_of_nutrient_medium}\n')
    recipe.write(f'Концентрация агара(%): {agar_concentration}\n')
    recipe.write(f'Температура стерилизации(С): {sterilization_temperature}')
print('Файл recipe.txt успешно сформирован!')