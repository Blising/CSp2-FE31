"""
Мішуров Віталій Анатолійович ФЕ-31 
   Завдання
    12. Дан список, що складається з кортежів, в яких вказано ім’я та місто, наприклад,
    [('Andrii', 'Kyiv'), ('Nik', 'London'), ('Luba', 'Kyiv')]. Отримайте словник, де ключами будуть
    міста, а значеннями - списки імен людей що живуть в даному місті.
"""
AllArrays = [('Anrii', 'Kiev'), ('Nik', 'London'), ('Sasha', 'India')]
people_cities={}
# for person,city in AllArrays:
#    if city not in  people_cities:
#     people_cities[city]= []
#     people_cities[city].append(person)
#     print(people_cities)
for person, city in AllArrays:
    people_cities[person] = city
    def get_city_by_name(name):
        return people_cities.get(name,"City not found ")
    name = input ("Enter the name:")
    print("City:", get_city_by_name(name))    



