
 
# мае меню 
main_menu= '''\n главное меню: 
     1. Показать контакт
     2. Добавить контакт 
     3. найти контакт 
     4. изменить контакт
     5. удолить контакт
     6. выход\n  ''' 

input_choice =  'выберите пункт меню: '

load_successful = 'телефонная книга успешно открыта! '

pb_empty =  'телефонная кнтга пуста или не загружена! '

input_new_contact = 'введите данные нового конткта: '

new_contact =  { 'name:' ,'введите имя: ','phone:', 'введите номер:','введите коментарий:','comment:'}

def new_contact_successful(name: str):
    return f'контакт {name}успешно добавлен'

input_search =  'что будем искать: '
def empty_search(word)->str:
    return f'контакты содержащиеслова"{word}"не найдены'

input_change =  'какой контакт будем менять: '


input_index = 'введите индекс контакта: '

change_contact =  'введите новые данные или оставьте поле пустым, что бы не менять: '

def change_successful(name:str)->str:
    return f'контакт {name} успешно изменен!'

    

