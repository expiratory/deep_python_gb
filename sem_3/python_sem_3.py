"""
Задача с семинара про друзей и поход
"""

friends_stuff = {
    "Андрей": ("палатка", "рюкзак", "фонарик"),
    "Борис": ("палатка", "компас", "фонарик"),
    "Виктор": ("палатка", "рюкзак", "вода")
}

# Вещи, которые взяли все друзья
all_friends_stuff = set(friends_stuff["Андрей"])
for stuff in friends_stuff.values():
    all_friends_stuff &= set(stuff)
print("Вещи, которые взяли все друзья:", all_friends_stuff)

# Уникальные вещи
unique_stuff = set()
for friend, stuff in friends_stuff.items():
    temp_stuff = set(stuff)
    for other_stuff in friends_stuff.values():
        if stuff != other_stuff:
            temp_stuff -= set(other_stuff)
    unique_stuff |= temp_stuff
print("Уникальные вещи:", unique_stuff)

# Вещи у всех кроме одного
for friend, stuff in friends_stuff.items():
    missing_items = set()
    for other_stuff in friends_stuff.values():
        if stuff != other_stuff:
            missing_items |= set(other_stuff) - set(stuff)
    for item in missing_items:
        print(f"У {friend} нет {item}")

"""
Задача 1
"""

def get_duplicates(lst):
    return list({x for x in lst if lst.count(x) > 1})

lst = [1,2,3,2,1,5,6,5,5,5]
print(get_duplicates(lst))

"""
Задача 2
"""

text = ("Граф же Растопчин, который то стыдил тех, которые уезжали, то вывозил присутственные места, то выдавал никуда "
        "не годное оружие пьяному сброду, то поднимал образа, то запрещал Августину вывозить мощи и иконы, "
        "то захватывал все частные подводы, бывшие в Москве, то на ста тридцати шести подводах увозил делаемый "
        "Леппихом воздушный шар, то намекал на то, что он сожжет Москву, то рассказывал, как он сжег свой дом и "
        "написал прокламацию французам, где торжественно упрекал их, что они разорили его детский приют; то принимал "
        "славу сожжения Москвы, то отрекался от нее, то приказывал народу ловить всех шпионов и приводить к нему, "
        "то упрекал за это народ, то высылал всех французов из Москвы, то оставлял в городе г-жу Обер-Шальме, "
        "составлявшую центр всего французского московского населения, а без особой вины приказывал схватить и увезти "
        "в ссылку старого почтенного почт-директора Ключарева; то сбирал народ на Три Горы, чтобы драться с "
        "французами, то, чтобы отделаться от этого народа, отдавал ему на убийство человека и сам уезжал в задние "
        "ворота; то говорил, что он не переживет несчастия Москвы, то писал в альбомы по-французски стихи о своем "
        "участии в этом деле, — этот человек не понимал значения совершающегося события, а хотел только что-то "
        "сделать сам, удивить кого-то, что-то совершить патриотически-геройское и, как мальчик, резвился над "
        "величавым и неизбежным событием оставления и сожжения Москвы и старался своей маленькой рукой то поощрять, "
        "то задерживать течение громадного, уносившего его вместе с собой, народного потока.")

text = text.lower()

for char in ['.', ',', '!', '?', ';', ':']:
    text = text.replace(char, '')

words = text.split()

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
for i in range(min(10, len(sorted_words))):
    print(sorted_words[i])

"""
Задача 3
"""

items = {
    "палатка": 5,
    "рюкзак": 3,
    "вода": 2,
    "фонарик": 0.5,
    "компас": 0.3,
}


def fit_into_backpack(items, capacity):
    sorted_items = {k: v for k, v in sorted(items.items(), key=lambda item: item[1])}
    result = []
    total_weight = 0
    for item, weight in sorted_items.items():
        if total_weight + weight <= capacity:
            result.append(item)
            total_weight += weight
    return result


print(fit_into_backpack(items, 7))
