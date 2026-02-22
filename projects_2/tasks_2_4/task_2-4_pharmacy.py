capsules = int(input('Введите общее количество капсул: '))
packaging = int(input('Введите вместимость одной упаковки: '))
packaging_summary = capsules // packaging
remains_of_capsules = capsules % (packaging_summary * packaging)
print(f'--- Отчет фасовочного цеха ---\nПолных упаковок:\t{packaging_summary}\nОстаток капсул:\t{remains_of_capsules}')