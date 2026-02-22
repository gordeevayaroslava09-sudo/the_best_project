dna = input('Введите последовательность ДНК: ')
dna_up = dna.upper()
dna_len = len(dna_up)
count_A = dna_up.count('A')
percent_A = count_A / dna_len * 100
count_G = dna_up.count('G')
percent_G = count_G / dna_len * 100
count_T = dna_up.count('T')
percent_T = count_T / dna_len * 100
count_C = dna_up.count('C')
percent_C = count_C / dna_len * 100
print (f'=== Анализ последовательности ДНК ===\nВведите последовательность ДНК: {dna}\nПоследовательность в верхнем регистре: {dna_up}\nПодсчет нуклеотидов:\nA: {count_A}\nG: {count_G}\nC: {count_C}\nT: {count_T}\nПроцентное содержание нуклеотидов:\nA: {percent_A: .2f}%\nG: {percent_G: .2f}%\nC: {percent_C: .2f}%\nT: {percent_T: .2f}%\nОбщая длина: {dna_len} ')