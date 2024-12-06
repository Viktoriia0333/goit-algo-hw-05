from contact_handler import add_contact, charge_contact, show_all_contacts, show_phone


def parse_command(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    print('Hi, i am a bot-helper! How can i help you?')
    contacts = {}

    while True:
        user_input = input('Enter the command: ')
        command, *args = parse_command(user_input)

        if command in ['exit', 'close']:
            print('Good bye!')
            break

        elif command in ['hello', 'hi']:
            print('Hi!')

        else:
            match command:
                case 'add':
                    print(add_contact(args, contacts))
                case 'change':
                    print(charge_contact(args, contacts))
                case 'phone':
                    print(show_phone(args, contacts))
                case 'all':
                    print(show_all_contacts(contacts))
                case _:
                    print('Sorry, i don`t know command like that yet.')


if __name__ == '__main__':
    main()
