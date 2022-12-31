"""
3. Рефакторинг.
Дано: неоптимальный код.

Задание: оптимизировать следующий код.

sentences = ['капитан джек воробей',
             'капитан дальнего плавания',
             'ваша лодка готова, капитан']

cap_count = 0
for sentence in sentences:
    cap_count += sentence.count('капитан')

print(cap_count)
"""


def do_main():
    sentences = ['капитан джек воробей',
                 'капитан дальнего плавания',
                 'ваша лодка готова, капитан']

    cap_count = sum(map(lambda sentence: sentence.count('капитан'), sentences))
    print(cap_count)


if __name__ == "__main__":
    do_main()
