# lesson-3 example 2
# working with fanction and agruments

def chech_person(person_name, person_surname, person_birthdate, city_of_life, email, phone_number):
    """Function check person info


    person_name = Name of person,
    person_surname = Surname of person,
    person_birthdate = Date of birth person,
    city_of_life = The city where is living the person,
    email = email of person,
    phone_number = phone number of person
    """

    print({'имя пользователя': person_name, 'фамилия пользователя': person_surname, 'дата рождения пользователя': person_birthdate,
           'город проживания': city_of_life, 'email': email, 'номер телефона': phone_number})


chech_person(
    person_name=input("Введите имя пользователя: "),
    person_surname=input("Введите фамилию пользователя: "),
    person_birthdate=input("Введите дату рождения пользователя: "),
    city_of_life=input("Введите город в котором проживает пользователь: "),
    email=input("Введите адрес электронной почты пользователя: "),
    phone_number=input("Введите номер телефона пользователя: "))
