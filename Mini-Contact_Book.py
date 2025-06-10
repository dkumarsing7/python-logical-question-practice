contact_book = {
    'person1':{'name' : 'Deep', 'phone' : '7424899716', 'email' : 'dkumarsing7@gmail.com'},
    'person2':{'name' : 'Div', 'phone' : '1234567899', 'email' : 'div7@gmail.com'},
    'person3':{'name' : 'mit', 'phone' : '9876543211', 'email' : 'mit7@gmail.com'}
    }

# Displaying contact book entries
def display():
    for person, details in contact_book.items():
        print(f"{details['name']} - phone : {details['phone']} - emails : {details['email']}")


# Adding a new contact
def add_contact(name, phone, email):
    new_person = f'person{len(contact_book) + 1}'
    contact_book[new_person] = { 'name' : name, 'phone' : phone, 'email' : email}

def search(name):
    for person, details in contact_book.items():
        if details['name'].lower() == name.lower():
            print("Found ====> \n")
            print(f"{details['name']} - phone : {details['phone']} - emails : {details['email']}")
            break
    else:
        print("contact not founnd")
            
def delete(name):
    for person in contact_book.keys():
        if contact_book[person]['name'].lower() == name.lower():
            del contact_book[person]
            print(f"Contact {name} deleted successfully.")
            break
    else:
        print("contact not founnd")
        
def menu():
    print('''
        ------------------------------------------------------
        
        📒 Welcome to the Mini Contact Book!
        
        1. 📋 View all contacts

        2. ➕ Add new contacts (name, phone, email)

        3. 🔎 Search for a contact

        4. ❌ Delete a contact
        
        5. 📑 Menu (Show options again)
        
        6. 🚪 Exit
        
        ------------------------------------------------------
        ''')

    main()
    
def main():
    try:
        user = int(input("Enter a choice 1-4 : "))
    except Exception as e:
        print("Invalid choice, please select a valid option (1-4).")
        print("Please try again.")
        print('------------------------------------------------------')
        main()

    match (user):
        case (1):
            display()
            print()
            print('------------------------------------------------------')
            main()
            # comment: 
        case (2):
            add_contact(input('Enter a name : '), input('Enter a phone : '), input('Enter a email : '))
            print()
            print('------------------------------------------------------')
            main()
            # comment: 
        case (3):
            search(input("Enter Name to search in contact book : "))
            print()
            print('------------------------------------------------------')
            main()
            # comment: 
        case (4):
            delete(input("Enter Name to delete in contact book : "))
            print()
            print('------------------------------------------------------')
            main()
            # comment: 
        case(5):
            menu()
        case(6):
            print("Exiting the contact book.......\nGoodbye!")
            print('Thank you for using the contact book!')
            exit()
menu()
