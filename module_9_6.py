"""
особенности работы с функциями генераторами и оператором yield
"""
# функция-генератор all_variants(text), которая принимает строку text и возвращает объект-генератор,
# при каждой итерации которого будет возвращаться подпоследовательности переданной строки.

def all_variants(text):
    n = len(text)
    for length in range(1, n + 1):
        for start in range(n - length + 1):
            yield text[start:start + length]


a = all_variants("abc")
for i in a:
    print(i)
