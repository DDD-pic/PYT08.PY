import veiw
import model
import text





def start():
    while True:
        choice = veiw.main_menu()



        match choice:
            case 1:
                model.open_pb()
                veiw.print_message(text.load_successful)   
            case 2: 
                model.save_pb()
                veiw.print_massage(text.save_successful)  
            case 3:
                pb = model.get_pb()  
                veiw.print_contacts(pb,text.pb_empty)
            case 4:
                contact = veiw.input_contact(text.input_new_contact)
                name = model.add_contact(contact)
                veiw.print_message(text.new_contact_successful(name))
            case 5:   
                key_word = veiw.input_search(text.input_search)
                result = choice.search(key_word)
                veiw.print_contact(result,text.empty_search(key_word))
            case 6:
                key_word = veiw.input_search(text.input_chage)
                result =choice.search(key_word)
                if result:
                    if len (result) != 1:
                       veiw.print_contact(result, '')
                       current_id = veiw.input_search(text.input_index)
                    
                elif not result:  
                    veiw.print_message(text.empty_search(key_word)) 
                else:
                        current_id = result[0].get( 'id')
                        new_contact = veiw.input_contact(text.change_contact)  
                        name = model.change_contact(new_contact,current_id)

                 