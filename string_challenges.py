# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'.lower()
print(word.count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
count = 0
for i in word.lower():
    if i in 'ауоиэыяюеё':
        count += 1
print(f'гласных букв в слове: {count}')


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
list_se = sentence.split()
for f in list_se:
    print(f[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
avg_sent = len(sentence) / len(sentence.split())
print(avg_sent)