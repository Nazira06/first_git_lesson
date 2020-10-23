#найти сумму цифр трехзначного числа
namber=int(input())
hund=namber//100 #ищем кол_во сотен
print(hund)
tens=namber//10%10 #ищем кол_во дсятков
print(tens)
didits=namber%100%10#тщем кол-во единиц
print(didits)
print(hund+tens+didits)


