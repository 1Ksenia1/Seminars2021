import random
import math
n = 10
m = n #чтобы поделить списки пополам
i = 0
t = 0
a = []
b = []
k = []
d = []
e = []
#рандомные элементы
while n > 0:
    if(m >=n):
        i+=1
        a.append(i)
        b.append(i)
        k.append(i)
        d.append(i)
        e.append(i)
    n-=1

print("========================================")
print("First randomize mass")
print(a)
print("========================================")
print()
#сбросить настройки
ksr = 0 #количество сравнений
kper = 0 #количество перестановок
i = 0
j = 0
#пузырёк - метод сортировки массивов и списков путем последовательного сравнения и обмена соседних элементов, если предшествующий оказывается больше последующего.
#формула: (n*n)-n
t = 0
for i in range(0,len(a)):
    for j in range(0,len(a) - 1):
        if a[j] > a[j + 1]:
            a[j] = a[j + 1]
            a[j + 1] = t
            kper+=1
            j+=1
        ksr+=1
    i+=1
print("========================================")
print("Sub sort")
print("ksr =",ksr)
print("kper =",kper)
print(a)
print("========================================")
#сбросить настройки
ksr = 0
kper = 0
t = 0
i = 0
j = 1
#быстрая - деление массива на две части, в одной из которых находятся элементы меньше определённого значения, в другой – больше или равные. 
while  j < len(b):
   for i in range(len(b) - j):
       ksr+=1
       if b[i] > b[i + 1]:
           b[i], b[i + 1] = b[i + 1], b[i]
           kper+=1
   j += 1
print("========================================")
print("Quickly sort")
print("ksr =",ksr)
print("kper =",kper)
print(b)
print("========================================")
#сбросить настройки
ksr = 0
kper = 0
i = 0
j = 0
#вставки - это алгоритм сортировки, в котором все элементы массива просматриваются поочередно, при этом каждый элемент размещается в соответственное место среди ранее упорядоченных значений.
for i in range(i,len(d)):
    t = d[i]
    j = i - 1
    while j >= 0 and d[j] > t:
        d[j + 1] = d[j]
        kper+=1
        j-=1
        ksr+=1
    d[j + 1] = t
    ksr+=1
print("========================================")
print("Insert sort")
print("ksr =",ksr)
print("kper =",kper)
print(d)
print("========================================")
#сбросить настройки
ksr = 0
kper = 0
t = 0
i = 0
j = 0
#выборка -cначала ищется самый маленький элемент во втором. Он добавляется в конце первого. Таким образом алгоритм постепенно формирует список от меньшего к большему.
min_i = 0 #самый маленький элемент
for i in range(i,len(e)):
    vxod = 0
    min_i = i
    j = i + 1
    for j in range(j,len(e)):
        if e[j] < e[min_i]:
            min_i = j
            vxod = 1
        ksr+=1
    if vxod == 1:
        kper+=1
    t = e[i]
    e[i] = e[min_i]
    e[min_i] = t
print("========================================")
print("Select sort")
print("ksr =",ksr)
print("kper =",kper)
print(e)
print("========================================")
#сбросить настройки
ksr = 0
kper = 0
t = 0
#Шелла - Оптимизация достигается путем сравнения не только соседних элементов, но и элементов на определенном расстоянии, которое в течении работы алгоритма уменьшается.На последней итерации это расстояние равно 1.
j = 0
t = 0
step = (int)(len(k) // 2)
while step > 0:
    i = 0
    while i < len(k) - step:
        j = i
        while j + step <= len(k) and j >= 0 and k[j] >= k[j + step]:
            tmp = k[j]
            k[j] = k[j + step]
            k[j + step] = t
            j-=step
            kper+=1
        ksr+=1
        i+=1
    step = (int)(step / 2)
print("========================================")
print("Shell sort")
print("ksr =",ksr)
print("kper =",kper)
print(k)
print("========================================")
