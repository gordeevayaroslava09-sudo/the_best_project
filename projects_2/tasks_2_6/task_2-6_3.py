donor = input('Введите группу крови донора (I, II, III, IV): ').upper().strip()
recepient = input ('Введите группу крови рецепиента (I, II, III, IV): ').upper().strip()
if donor == 'II' and recepient == 'II':
    print('Переливать можно')
elif donor == 'III' and recepient == 'III':
    print('Переливать можно')
elif donor == 'IV' and recepient == 'IV':
    print('Переливать можно')
elif donor == 'I' and recepient == "I":
    print('Переливать можно')
elif donor == 'I' and recepient == 'II':
    print('Переливать можно')
elif donor == 'I' and recepient == 'III':
    print('Переливать можно')
elif donor == 'I' and recepient == 'IV':
    print('Переливать можно')
else:
    print('Переливание невозможно')