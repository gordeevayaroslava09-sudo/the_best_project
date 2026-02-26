seq = [ "ATATACGCGTA", "CTTCGGNGGA" ]
seq1 = 'ATATACGCGTA'+'CTTCGGNGGA'
print(f'Последовательность нуклеотидов целиком:\n{seq1}\n')
print()
print('Последовательность нуклеотидов построчно:\n')
for letter in seq1:
    print(letter)
print()
print('Цикл завершен')