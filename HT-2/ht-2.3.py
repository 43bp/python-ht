## Задача 3. Даны две строки. 
## Посчитайте сколько раз каждый символ первой строки встречается во второй
## «one» «onetwonine» - o – 2, n – 3, e – 2

string1 = "one"
string2 = "onetwonine"
string1x2 = set(string1) & set(string2)
print(len(string1x2))
print(', '.join(string1x2))