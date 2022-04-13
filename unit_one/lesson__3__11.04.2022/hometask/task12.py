#Единицы массы пронумерованы следующим образом: 1 — килограмм, 2 — миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер.
#Дан номер единицы массы и масса тела M в этих единицах (вещественное число). Вывести массу данного тела в килограммах.
# Данную задачу нужно решить с помощью конструкции  match  (Python v3.10)


# Пример:
# Введите единицу массы тела
#       1 - килограмм
#       2 — миллиграмм
#       3 — грамм
#       4 — тонна
#       5 — центнер
#>4

#Введите  массу тела
#>1
#Ответ: 1000 кг

print("Единицы массы пронумерованы следующим образом:")
print("1 - килограмм")
print("2 — миллиграмм")
print("3 — грамм")
print("4 — тонна")
print("5 — центнер")

vvod = int(input("Введите единицу массы тела:"))

def road_to_kilogramms(vvod):
    match vvod:
        case 1:
            massa_tela = int(input("Введите массу тела:"))
            print("Масса тела:", massa_tela, "кг")
        case 2:
            massa_tela = int(input("Введите массу тела:"))
            massa_tela = massa_tela / 10 ** 6
            print("Масса тела в:", massa_tela, "кг")
        case 3:
            massa_tela = int(input("Введите массу тела:"))
            massa_tela = massa_tela / 1000
            print("Масса тела в:", massa_tela, "кг")
        case 4:
            massa_tela = int(input("Введите массу тела:"))
            massa_tela = massa_tela * 1000
            print("Масса тела в:", massa_tela, "кг")
        case 5:
            massa_tela = int(input("Введите массу тела:"))
            massa_tela = massa_tela * 100
            print("Масса тела в:", massa_tela, "кг")
        case _:
            print("Неверный тип данных. Перезапустите программу.")
road_to_kilogramms(vvod)