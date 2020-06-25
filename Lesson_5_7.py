"""7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков)."""

average_profit = 0
firm_dict = {}
count = 0
with open('file_5_7', 'r') as firm:
    while True:
        try:
            name_firm, _, revenue, cost = firm.readline().split()
        except ValueError: break
        count += 1
        incom = int(revenue) - int(cost)
        firm_dict[name_firm] = incom
        if incom > 0:
            average_profit += incom
        else: count -= 1
    average_profit = round(average_profit / count, 3)
    firm_dict['average_profit'] = average_profit
print(firm_dict)