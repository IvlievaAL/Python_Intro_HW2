# Задача 14: Требуется вывести все целые степени двойки 
# (т.е. числа вида 2k), не превосходящие числа N
N=int(input ("Введите неотрицательное число"))
stepeni2=list()
k=0
while N>=2^k:
    stepeni2.append(2^k)
    k+=1
print(stepeni2)