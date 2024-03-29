Источник:[https://aliev.me/runestone/](https://aliev.me/runestone/)

Упражнения:

1. Реализуйте простые методы getNum и getDen, возвращающие числитель и знаменатель дроби.
2. Во многих отношениях было бы лучше, если бы все дроби приводились в сокращённом виде с самого начала. 
Измените конструктор класса Fraction таким образом, чтобы GCD с самого начала использовался для сокращения 
дробей. Заметьте, это означает, что функция __ add __ больше не нуждается в сокращениях. Произведите 
необходимые модификации.
3. Реализуйте оставшиеся простые арифметические операторы (__ sub __, __ mul __ и __ truediv __).
4. Реализуйте оставшиеся операторы отношений (__ gt __, __ ge __, __ lt __, __ le __, and __ ne __)
5. Модифицируйте конструктор класса дробей таким образом, чтобы он поверял, являются ли числитель и 
знаменатель целыми числами. Если хотя бы одно из условий не выполняется, то вызовите исключение.
6. В определении дробей мы предположили, что отрицательные дроби имеют отрицательный числитель и 
положительный знаменатель. Использование отрицательного знаменателя может повлечь за собой неправильные 
результаты некоторых операторов отношений. Вообще, это ограничение является не таким уж необходимым. 
Модифицируйте конструктор таким образом, чтобы пользователь мог вводить отрицательный знаменатель, 
а все операторы продолжали работать правильным образом.
7. Исследуйте метод __ radd __. В чём его отличие от __ add __? Когда он используется? Реализуйте __ radd __.
8. Задание аналогично предыдущему, но на этот раз рассмотрите метод __ iadd __.
9. Исследуйте __ repr __ метод. Чем он отличается от __ str __? Когда используется? Реализуйте __ repr __.
10. Исследуйте другие типы существующих вентилей (таких как NAND(НЕ-И), NOR(НЕ-ИЛИ) и исключающее XOR(ИЛИ)). 
Добавьте их в иерархию цепей. Сколько дополнительного кода вам понадобилось?
11. Наиболее простая арифметическая цепь называется полусумматор. Исследуйте и реализуйте её.
12. Теперь расширьте эту цепь и реализуйте 8-битный полный сумматор.
13. Симуляция цепи, показанная в данной части, работает в обратном направлении. Другими словами, выходное 
значение вычисляется с помощью обратного прохода через входные значения, которые в свою очередь запрашивают 
свои выходы. Это продолжается до тех пор, пока очередь не дойдёт до внешних входных линий. Именно в этот 
момент значения для них будут запрошены у пользователя. Измените реализацию таким образом, чтобы эти 
действия происходили в прямом направлении: схема вычисляла занчение выхода после получения данных на входах.
14. Создайте класс, представляющий игровые карты. Потом создайте класс, представляющий колоду карт. 
Используя эти два класса, реализуйте вашу любимую карточную игру.
15. Найдите головоломку Судоку в местной газете. Напишите программу для её решения.