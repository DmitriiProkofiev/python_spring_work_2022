# todo: Дан номер некоторого года (положительное целое число).
# Вывести соответствующий ему номер столетия, учитывая, что, к примеру, началом 20 столетия был 1901 год.
print("Введите год:")

god = int(input())
if (god % 100 > 0):
   stoletie = god // 100 + 1
else:
   stoletie = god // 100

print("Этот год относится к", stoletie, "-му столетию.")