import random
import re

inputData = list()
outputData = list()
f = open('text.txt')
line = f.readline()
inputData = re.split(', | \n', line)  # массив с элементами
inputData.pop()
n = int(f.readline())   # размер кеша

hash = dict()
cache = list()

print('\n LRU\n')
#LRU
outputData.append('LRU ')
oldList = list()
for i in inputData:
    oldList.clear()
    for j in cache:
        oldList.append(j)
    if i not in cache:
        if cache.__len__() < n:
            cache.append(i)
        else:
            cache.pop(0)
            cache.append(i)
    if oldList == cache:
        outputData.append('1')
    else:
        outputData.append('0')

outputData.append('\nMark ')
print('\n MARK\n')
#Mark
oldHash = dict()
for i in inputData:
    oldHash.clear()
    for j in hash.keys():
        elem = hash[j]
        oldHash[j] = elem
    if i not in hash.keys():
        if len(hash) < n:
            hash[i] = 0
        else:
            while True:
                keys = hash.keys()
                item = random.choice(list(keys))
                if hash[item] == 0:
                    hash.pop(item)
                    break
            hash[i] = 0
    else:
        if hash[i] != 1:
            hash[i] = 1
        else:
            full_cache = True
            for j in hash.keys():
                if hash[j] == 0:
                    full_cache = False
                    break
            if full_cache == True:
                for j in hash.keys():
                    hash[j] = 0
    if oldHash == hash:
        outputData.append('1')
    else:
        outputData.append('0')

outputData.append('\nMPI ')
print('\n MPI \n')
#  MPI задааем количество элементов в кеш и потом сами распределяем по хот и колд исходя лимита который заранее задем
hash.clear()
boarder = 250  # значение для разграничесния хот и колд зоны
increase = 50  # на сколько увеличиваем значения
countHot = 0   # разграничение хот и колд зоны в кеше
cacheOrder = list()  # список для хранения КЭШ в нужной последовательности
for i in inputData:
    oldList.clear()
    for j in cacheOrder:
        oldList.append(j)
    if i not in hash:
        if hash.__len__() < n:
            hash[i] = 1
            cacheOrder.append(i)
        else:
            num = cacheOrder.pop(0)
            hash.pop(num)
            hash[i] = 1
            cacheOrder.insert(cacheOrder.__len__() - countHot, i)  # вставляем элемент в список в конец колд хоны
    else:
        num = hash[i]
        hash[i] = num * increase
        if hash[i] > boarder: # если значение больше границы то оно добавляется в хот зону
            index = cacheOrder.index(i)
            cacheOrder.pop(index)
            cacheOrder.insert(cacheOrder.__len__()-countHot, i)
            countHot += 1
    if random.randint(1, 100) % 2 == 0: # рандомно уменьшаем ВСЕ счетчики
        for j in hash.keys():
            hash[j] /= 2
            index = cacheOrder.index(j) # получаем ПОРЯДКОВЫЙ НОМЕР элемента в списке чтобы знать в какой он зоне
            if (hash[j] < boarder) and (index > cacheOrder.__len__() - countHot): # проверка для элемента колд зоны
                cacheOrder.pop(index)
                cacheOrder.insert(0, j)
                countHot -= 1
    #print(hash)
    #print(cacheOrder)
    if oldList == cacheOrder:
        outputData.append('1')
    else:
        outputData.append('0')

f = open('output.txt', 'w')
for index in outputData:
    f.write(index)








