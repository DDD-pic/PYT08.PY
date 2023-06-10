
 
# хранение текста
#path = "phon.txt" 
#data = open(path, "w") 
#for line in data:
#   print(line)
#data.close()
 
# мае меню 
#main_menu= ('''\n главное меню: 
#     1. Показать контакт
#     2. Добавить контакт 
#     3. найти контакт 
#     4. изменить контакт
#     5. удолить контакт
#     6. выход\n  ''' )
#print(main_menu)
#print("выбрать пункт меню: ")

def open_file_read(path):
    with open(path, 'r') as file:
        main_list=(file.readline()) 
        main_list_str = [x.split( ':') for x in main_list]
    return main_list_str
print(open_file_read("phon.txt"))