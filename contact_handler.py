def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return 'There is no this contact in your contacts list'
        except IndexError:
            return 'Enter the arguments'

    return inner


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return 'contact added'


@input_error
def charge_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return 'Successfully changed'
    else:
        raise KeyError


@input_error
def show_phone(args: str,  contacts: dict):
    name = args[0]
    return contacts[name]


@input_error
def show_all_contacts(contacts):
    return contacts