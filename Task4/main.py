#Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
#Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое 
#количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
#*Пример:*
#6 -> 1  4  1
#24 -> 4  16  4
#    60 -> 10  40  10

a = int (input ("Введите число журавликов: "))
n=0
n_Petya=int(a/6)
n_Serega=int(n_Petya)
n_Katya= int(n_Petya*4)
print("Петя сделал журавликов: ", n_Petya)
print("Сережа сделал журавликов: ", n_Serega)
print("Катя сделала журавликов: ", n_Katya)
