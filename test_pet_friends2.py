from api import PetFriends
from settings import valid_email,valid_password
import os

pf=PetFriends()

def test_add_new_pet_with_nulltype (name='Бабака', animal_type='',age='4'):
#проверка ошибки при добавлении питомца с пустым типом
#не должен принимать пустой тип питомца
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_simple(auth_key, name, animal_type, age)
    assert status == 400

def test_add_new_pet_without_name (name='', animal_type='Собака',age='4'):
#проверка ошибки при добавлении питомца с пустым именем
#не должен принимать пустое имя
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_simple(auth_key, name, animal_type, age)
    assert status == 400

def test_get_api_key_for_invalid_user(email='12345@mail.ru',password='12345678'):
    #проверка авторизации в некорректным email
    status,result=pf.get_api_key(email,password)
    assert status==403

def test_get_api_key_for_invalid_password(email=valid_email,password='87654'):
    #проверка авторизации с некорректным паролем
    status,result=pf.get_api_key(email,password)
    assert status==403

def test_get_api_key_for_nullpassword(email=valid_email,password=''):
    #проверка авторизации пустым паролем
    status,result=pf.get_api_key(email,password)
    assert status==403

def test_add_new_pet_without_photo(name='Святлячек2', animal_type='собака',age='4', pet_photo=''):
    #проверка ошибки при добавлении питомца без фото
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400

def test_fail_update_pet_info_nulltype(name='Володя', animal_type='', age=5):
#позволяет обновить тип питомца на пустой

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Если список не пустой, то пробуем обновить его имя, тип (на пустой) и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        assert status == 400
    else:
        raise Exception("There is no my pets")

def test_fail_update_pet_info_invalid_age(name='Володя', animal_type='собака', age=-5):
#позволяет обновить возраст на отрицательный

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Если список не пустой, то пробуем обновить его имя, тип (на пустой) и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        assert status == 400
    else:
        raise Exception("There is no my pets")

def test_add_new_pet_with_invalid_age(name='Святлячек2', animal_type='собака',age='-4', pet_photo='tests/images/11.jpg'):
    #добавление животного с отрицательным возрастом
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 400

def test_successful_update_self_pet_photo (pet_photo='tests/images/12.jpeg'):
#проверка обновления фото
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Еслди список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_photo(auth_key, my_pets['pets'][0]['id'], pet_photo)
        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status == 200
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")







