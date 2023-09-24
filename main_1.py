phonebook = {}

def main():
    while True:
        user_input = input()
        splitted_input = user_input.split()
        user_input = user_input.lower()

        if user_input.startswith('hello'):
            print(hello_mesage())    
        elif user_input.startswith('add'):
            print(add(splitted_input[1:])) 
        elif user_input.startswith('change'):
            print(change(splitted_input[1:])) 
        elif user_input.startswith('phone'):
            print(phone(splitted_input[1:])) 
        elif user_input.startswith('show all'):
            print (show_all())
        elif user_input.startswith('exit') or user_input.startswith('good bye') or user_input.startswith('close'):
            print(exit())
            break
        else: 
            print(error())

def input_error(input_func):
    def output_func(*args):
        try:
            result = input_func(*args) 
        except KeyError:
            result = 'No such user name in phonebook'
        except ValueError:
            result = 'Invalid format of number phone'
        except IndexError:
            result = 'You not provide all necessery parameter'
        return result
    return output_func

def hello_mesage():
    return 'How can I help you?'

@input_error
def add(contact):
    phonebook.update({contact[0]: int(contact[1])})
    return 'contact added successfully'

@input_error
def change(contact):
    if contact[0] in phonebook:
        phonebook[contact[0]] = int(contact[1])
        return 'contact updated successfully'
    else:
        raise KeyError
    
@input_error
def phone(contact):
    if contact[0] in phonebook:
        return phonebook[contact[0]]
    else:
        raise KeyError
    
def show_all():
    return phonebook

def exit():
    return 'Good bye!'

def error():
    return 'not supported command'

if __name__ == '__main__':
    main()