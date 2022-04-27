#todo: Создайте функцию compute_bill, считающаю итоговую сумму товаров в чеке.
# Функция должна принимать 1 параметр - словарь, в котором указано количество едениц товара.
# Цены хранятся в словаре:
# prices = {
#   "banana": 4,
#   "apple": 2,
#   "orange": 1.5,
#   "pear": 3
# }

prices = {"Банан": 4, "Яблоко": 2, "Апельсин": 1.5, "Персик": 3}


def compute_bill(prices_):
  chek = dict()
  summ = 0
  for key in prices_:
    print(key)
    chek[key] = float(input("Введите количество: ")) * prices_[key]
    summ += chek[key]

  return summ

print("Итог: ", compute_bill(prices))