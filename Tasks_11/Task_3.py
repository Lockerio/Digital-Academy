"""
3. Рефакторинг.
Дано: неоптимальный код.

Задание: оптимизировать следующий код.

def responses_creator(item_ids):
    item_ids = [None] if item_ids is None else item_ids

    responses = []
    for item_id in item_ids:
        new_response = dict(item_id=item_id)
        responses.append(new_response)
    return responses
"""


def responses_creator(item_ids):
    if not item_ids:
        return {'item_id': None}
    responses = [
        {
            'item_id': item
        }
        for item in item_ids
    ]
    return responses


if __name__ == '__main__':
    print(responses_creator([1, 5, 7]))
    print(responses_creator(None))
