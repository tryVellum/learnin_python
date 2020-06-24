"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке."""
count = 0
my_dict = {}
with open('file_5_2', 'r') as data:
    lines = len(data.readlines())
    data.seek(0)
    for i in range(1, lines + 1):
        my_dict[i] = len(data.readline().split())

for itm in my_dict:
    print(f'{itm}-ая строчка содержит {my_dict[itm]}')