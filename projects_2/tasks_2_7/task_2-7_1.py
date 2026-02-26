files = ["seq1", "seq2", "seq3", "seq4"]
data = input('Введите дату: ')
for name in files:
    new_name = name + f".fasta - {data}"
    print(f"{new_name}")