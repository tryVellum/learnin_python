"""2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой."""

def sucurity_information(name, secName, yers, city, email, mobile_number):
    print(f'{name} {secName} {yers} {city} {email} {mobile_number}')

n = "Clint"
s = "Eastwood"
y = 1930
c = "San-Francisco"
e = "realclinteastwood@google.com"
m = "+16507599755"

sucurity_information(name=n, secName=s, yers=y, city=c, email=e, mobile_number=m)
