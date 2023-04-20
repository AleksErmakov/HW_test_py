def geo_logs_visit(my_visits):
    new_geo_logs = []
    for elem in my_visits:
        for my_visit, my_country in elem.items():
            if "Россия" in my_country:
                new_geo_logs.append(elem)
    return new_geo_logs


def unique_id(some_id):
    result = []
    for item in some_id.values():
        for elem in item:
            if elem not in result:
                result.append(elem)
    return result


def biggest_volume_channel(some_dict):
    max_volume = max(some_dict.values())
    name_channel = max(some_dict, key=some_dict.get)
    return f'{name_channel}: {max_volume}'


geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

stats = {'facebook': 55, 'yandex': 120, 'vk': 15, 'google': 99, 'email': 112, 'ok': 12}

# print(geo_logs_visit(geo_logs))
# print(unique_id(ids))
# print(biggest_volume_channel(stats))
